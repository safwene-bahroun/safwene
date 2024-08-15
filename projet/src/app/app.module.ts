import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { YourAbsenceComponent } from './your-absence/your-absence.component';
import { HttpClientModule, provideHttpClient, withFetch } from '@angular/common/http';
import { AuthService } from './auth.service';
import { AbsencesService } from './absences.service';
import { SignComponent } from './sign/sign.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    SignComponent,
    YourAbsenceComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [
    AuthService,
    AbsencesService,
    provideHttpClient(withFetch())
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

