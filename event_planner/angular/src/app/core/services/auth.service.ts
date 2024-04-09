import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs';
import { ApplicationUser } from '../models/application-user';
import { environment } from '../../../environments/environment';

interface LoginResult {
  username: string;
  role: string;
  access_token: string;
  token_type: string;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly apiUrl = environment.apiUrl + `user`;
  constructor(private router: Router, private http: HttpClient) {}

  get user(): ApplicationUser {
    const u = localStorage.getItem('user');
    if (!u) {
      return {
        username: '',
        role: '',
        token: '',
      };
    }
    return JSON.parse(u);
  }

  signup(username: string, password: string) {
    return this.http.post(`${this.apiUrl}/signup`, {
      email: username,
      password,
    });
  }

  login(username: string, password: string) {
    let formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    return this.http.post<LoginResult>(`${this.apiUrl}/sign-in`, formData).pipe(
      map((x) => {
        localStorage.setItem(
          'user',
          JSON.stringify({
            username: username,
            role: x.role,
            token: x.access_token,
          })
        );
        return x;
      })
    );
  }

  logout() {
    localStorage.setItem(
      'user',
      JSON.stringify({
        username: '',
        role: '',
        token: '',
      })
    );
    this.router.navigate(['login']);
  }
}
