import { Component, OnInit, OnDestroy } from '@angular/core';
import { Socket } from 'ngx-socket-io';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent // implements OnInit, OnDestroy 
{
  // constructor(private socket: Socket) {

  // }
  // ngOnInit() {
  //   //this.socket.connect();

  //   this.socket.on('chat_message', (message: string) => {
  //     this.handleMessage(message)
  //   })
  // }
  // handleMessage(message: string) {
  //   console.log(message);
  // }
  // sendMessage(message: string) {
  //   this.socket.emit('chat_message', message);
  // }
  // ngOnDestroy() {
  //   this.socket.disconnect();
  // }

}
