import { Component } from '@angular/core';
import { AbsencesService } from '../absences.service';
@Component({
  selector: 'app-your-absence',
  templateUrl: './your-absence.component.html',
  styleUrl: './your-absence.component.css'
})
export class YourAbsenceComponent {
  
  absences: any[] = [];
  profile: any;
  constructor(private absencesService: AbsencesService) {}
  getAbsences(cin: string) {
    this.absencesService.getAbsences(cin).subscribe(
      data => {
        this.absences = data;
      },
      error => {
        console.error('Error fetching absences', error);
      }
    );
  }

  getProfile(etudiant_id: number) {
    this.absencesService.getProfile(etudiant_id).subscribe(
      data => {
        this.profile = data;
      },
      error => {
        console.error('Error fetching profile', error);
      }
    );
  }




}
