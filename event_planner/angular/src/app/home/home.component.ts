import { Component, OnInit } from '@angular/core';
import { ApplicationUser, AuthService } from '../core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  user!: ApplicationUser;
  expiry: Date = new Date();

  constructor(authService: AuthService) {
    this.user = authService.user;
    const accessToken = this.user.token;
    if (accessToken) {
      const jwtToken = JSON.parse(atob(accessToken.split('.')[1]));
      this.expiry = new Date(jwtToken.expires * 1000);
    }
  }

  ngOnInit(): void {}
}
