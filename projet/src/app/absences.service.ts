import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class AbsencesService {
  private baseUrl = 'http://localhost:5000/absences';

  constructor(private http: HttpClient) {}

  getAbsences(cin: string): Observable<any> {
    let params = new HttpParams().set('cin', cin);
    return this.http.get(`${this.baseUrl}/`, { params });
  }

  getProfile(etudiant_id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/profile/${etudiant_id}`);
  }

}
