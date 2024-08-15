import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  email ='';
  password ='';
  border ='1';
  color ='green';
emailpattern ="[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$";

 credentials = { email: '', password: '' };

  constructor(private authService: AuthService) {}

  login() {
    this.authService.login(this.credentials).subscribe(
      response => {
        console.log('Login successful', response);
      },
      error => {
        console.error('Login failed', error);
      }
    );
  }





}
