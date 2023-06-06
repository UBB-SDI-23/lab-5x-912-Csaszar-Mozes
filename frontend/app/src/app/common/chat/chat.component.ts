import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { Message, MessageModel } from 'src/app/models/models';

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
      c_obj.handleMessageDown(e);
    });

    this.messageInput1.addEventListener('keyup', (e) => {
      c_obj.handleMessageUp(e);
    });

    this.socket.onmessage = function (e) {
      const data = JSON.parse(e.data)['message'] as MessageModel;
      c_obj.addMessageToBox(data);
    }

    this.socket.onclose = function (e) {
      alert("Chat server closed unexpectedly.");
    }

    this.populateMessagebox();
  }
  populateMessagebox() {
    this.apiServ.getMessages(15).subscribe(
      (ret) => {
        let messages = ret as MessageModel[];
        messages.sort((a, b) => a.id! < b.id! ? -1 : 1)
        for (let m of messages) {
          this.addMessageToBox(m);
        }
      }
    )
  }
  addMessageToBox(m: MessageModel) {
    this.messageBox.innerHTML += "<b>" + m['nickname'] + "</b><br>";
    this.messageBox.innerHTML += m['content'] + '<br>';
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
  handleMessageUp(e: KeyboardEvent) {
    if (e.key != 'Enter') {
      if (e.key == ' ') {
        this.getNewSuggestion();
      }
      else {
        this.removeSuggestion();
      }
    }
  }
  // Send message on pressing enter
  handleMessageDown(e: KeyboardEvent) {
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

  }
  sendMessage() {
    let nickname: string = this.nicknameFormControl.value;
    let content: string = this.messageInput1!.value;
    if (content.length > 300) {
      alert("Message too long!")
    }
    else if (content.trim() != '' && nickname != '') {
      let m: MessageModel = new MessageModel();
      m.content = content;
      m.nickname = nickname;
      this.apiServ.addMessage(m).subscribe(
        () => {
          this.socket.send(JSON.stringify({
            'message': {
              'content': m.content,
              'nickname': m.nickname
            }
          }));
          this.messageInput1!.value = '';
          this.messageInput2!.value = '';
        }
      );
    }
  }
}
