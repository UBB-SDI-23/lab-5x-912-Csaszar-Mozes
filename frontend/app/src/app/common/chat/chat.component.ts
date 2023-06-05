import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ManageAccountService } from 'src/app/api/manage-account-service';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements OnInit {
  static socketURL: string = "ws://127.0.0.1:8000/ws/chat/general/"
  public socket: WebSocket = new WebSocket(ChatComponent.socketURL);
  public dataString: string = '';
  private messageBox!: HTMLElement;
  messageFormControl: FormControl = new FormControl('', [Validators.maxLength(100)])
  nicknameFormControl: FormControl = new FormControl('', [Validators.maxLength(100)]);

  constructor(protected manageAccountServ: ManageAccountService) { }

  ngOnInit() {
    this.messageBox = document.getElementById('MessagesChatBox') as HTMLElement;
    let c_obj: ChatComponent = this;
    this.nicknameFormControl.setValue(this.manageAccountServ.getNickname());
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
  // Send message on pressing enter
  handleMessage(e: KeyboardEvent) {
    if (e.key == 'Enter') {
      this.sendMessage();
    }
  }
  sendMessage() {
    let userName: string = this.nicknameFormControl.value;
    let message: string = this.messageFormControl.value;
    if (message.trim() != '') {
      this.socket.send(JSON.stringify({
        'message': {
          'message': this.messageFormControl.value,
          'user': userName
        }
      }));
      this.messageFormControl.setValue('');
    }
  }
}
