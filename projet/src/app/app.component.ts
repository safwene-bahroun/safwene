import { Component, OnInit } from '@angular/core';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  title="projet";
 
  constructor(private authService: AuthService) {}
  isLoggedIn = true;
  logout() {
    this.authService.logout().subscribe(
      response => {
        console.log('Logged out successfully', response);
        this.isLoggedIn = false;
      },
      error => {
        console.error('Logout failed', error);
      }
    );
  }
  ngOnInit(): void {

}
}