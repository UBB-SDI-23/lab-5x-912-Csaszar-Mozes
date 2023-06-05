import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { Message } from 'src/app/models/models';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  static socketURL: string = APIService.webSocketUrl() + "/ws/chat/general/";
  public socket: WebSocket = new WebSocket(ChatComponent.socketURL);
  public dataString: string = '';
  private messageBox!: HTMLElement;
  messageFormControl: FormControl = new FormControl('', [Validators.maxLength(100)]);
  underlayMessageFormControl: FormControl = new FormControl();
  nicknameFormControl: FormControl = new FormControl('', [Validators.maxLength(100)]);

  messageInput1: HTMLInputElement | undefined;
  messageInput2: HTMLInputElement | undefined;
  nextSuggestion: string = '';
  handledEnter: boolean = false;

  constructor(protected manageAccountServ: ManageAccountService, protected apiServ: APIService) { }

  ngOnInit() {
    this.messageBox = document.getElementById('MessagesChatBox') as HTMLElement;
    let c_obj: ChatComponent = this;
    this.nicknameFormControl.setValue(this.manageAccountServ.getNickname());
    this.messageInput1 = document.getElementById("message") as HTMLInputElement;
    this.messageInput2 = document.getElementById("message2") as HTMLInputElement;

    this.messageInput1.addEventListener('keydown', (e) => {
      c_obj.handleMessage(e);
    })

    this.socket.onmessage = function (e) {
      const data = JSON.parse(e.data)['message'];
      c_obj.dataString += "<b>" + data['user'] + "</b><br>";
      c_obj.dataString += data['message'] + '<br>';
      c_obj.messageBox.innerHTML = c_obj.dataString;
    }

    this.socket.onclose = function (e) {
      alert("Chat server closed unexpectedly.");
    }
  }

  saveNickname() {
    if (this.nicknameFormControl.valid) {
      this.manageAccountServ.saveNickname(this.nicknameFormControl.value);
    }
    else {
      alert("Nickname too long!");
      this.nicknameFormControl.setValue((this.nicknameFormControl.value as string).slice(0, (this.nicknameFormControl.value as string).length - 1));
    }
  }
  getNewSuggestion() {
    this.apiServ.getSuggestion(this.messageInput1!.value).subscribe(
      (value: Message) => {
        this.nextSuggestion = value.message!;
        this.messageInput2!.value = this.messageInput1!.value + this.nextSuggestion;
      }
    )
  }
  removeSuggestion() {
    this.nextSuggestion = "";
    this.messageInput2!.value = this.messageInput1!.value;
  }
  // Send message on pressing enter
  handleMessage(e: KeyboardEvent) {
    if (e.key == 'Enter') {
      if (this.nextSuggestion == "") {
        this.handledEnter = false;
        this.sendMessage();
      }
      else {
        e.preventDefault();
        this.handledEnter = true;
        this.messageInput1!.value += this.nextSuggestion + " ";
        this.getNewSuggestion();
      }

    }
    else if (e.key == ' ') {
      this.getNewSuggestion();
    }
    else {
      this.removeSuggestion();
    }
  }
  sendMessage() {
    let userName: string = this.nicknameFormControl.value;
    let message: string = this.messageInput1!.value;
    if (message.trim() != '') {
      this.socket.send(JSON.stringify({
        'message': {
          'message': this.messageInput1!.value,
          'user': userName
        }
      }));
      this.messageInput1!.value = '';
      this.messageInput2!.value = '';
    }
  }
}
