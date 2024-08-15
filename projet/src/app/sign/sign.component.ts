import { Component } from '@angular/core';
import { AuthService } from '../auth.service'; // Adjust the path as necessary

@Component({
  selector: 'app-sign',
  templateUrl: './sign.component.html',
  styleUrls: ['./sign.component.css']
})
export class SignComponent {
  image = 'assets/images/pr.jpeg'; // Adjusted path
  user: any = {
    cin: '',
    nom: '',
    prenom: '',
    email: '',
    classes: 'choose option',
    filiere: 'choose option'
  };
  color: any = {
    nom: '',
    prenom: '',
    cin: '',
    email: '',
    password :'',
    classes : '',
    filiere :'',
  };
  password: string = '';
  submitted = false;
  emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  constructor(private authService: AuthService) {}

  getColor(control: string): string {
    return this.color[control] || '';
  
}

  update() {
    this.color.nom = this.user.nom ? 'success' : 'error';
    this.color.prenom = this.user.prenom ? 'success' : 'error';
    this.color.cin = this.user.cin.length >= 8 ? 'success' : 'error';
    this.color.email = this.user.email.match(this.emailPattern) ? 'success' : 'error';
    this.color.password = this.password.match(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/) ? 'success' : 'error';
    this.color.classes = this.user.classes && this.user.classes !== 'choose option' ? 'success' : 'error';
    this.color.filiere = this.user.filiere && this.user.filiere !== 'choose option' ? 'success' : 'error';
  }
  onSubmit(form: any) {
    if (form.valid) {
      this.submitted = true;
      if (Object.values(this.color).every(c => c === 'success')) {
        this.register();
      } else {
        console.log('Form is valid but manual validation failed');
      }
    } else {
      this.submitted = false;
      console.log('Form is invalid');
    }
  }
  register() {
    this.authService.register(this.user).subscribe(
      response => {
        console.log('User registered successfully', response);
      },
      error => {
        console.error('Registration error', error);
      }
    );
  }







}
