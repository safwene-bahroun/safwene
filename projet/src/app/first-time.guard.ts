import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FirstTimeGuard implements CanActivate {

  constructor(private router: Router) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): Observable<boolean> {
    if (typeof window !== 'undefined') {
      const hasVisited = localStorage.getItem('hasVisited');

      if (!hasVisited) {
        localStorage.setItem('hasVisited', 'true');
        if (state.url === '/') {
          return of(true);
        }
      }
      if (state.url === '/') {
        this.router.navigate(['/your-absence']);
        return of(false);
      }
    }
    return of(true);
  }
}
