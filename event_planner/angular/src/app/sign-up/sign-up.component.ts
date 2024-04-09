import { Component, OnInit } from '@angular/core';
import { finalize } from 'rxjs';
import { AuthService } from '../core';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrl: '../login/login.component.css',
})
export class SignUpComponent implements OnInit {
  busy = false;
  username = '';
  password = '';
  loginError = false;
  signupSuccess = false;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {}

  signup() {
    if (!this.username || !this.password) {
      return;
    }

    this.busy = true;
    this.authService
      .signup(this.username.trim(), this.password)
      .pipe(finalize(() => (this.busy = false)))
      .subscribe({
        next: () => {
          this.signupSuccess = true;
        },
        error: () => {
          this.signupSuccess = false;
          this.loginError = true;
        },
      });
  }
}
