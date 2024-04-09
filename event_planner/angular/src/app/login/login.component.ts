import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthService } from '../core';
import { finalize } from 'rxjs/operators';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  busy = false;
  username = '';
  password = '';
  loginError = false;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private authService: AuthService
  ) {}

  ngOnInit(): void {
    if (this.authService.user.token) {
      const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
      this.router.navigate([returnUrl]);
    }
  }

  login() {
    if (!this.username || !this.password) {
      return;
    }
    this.busy = true;
    const returnUrl = this.route.snapshot.queryParams['returnUrl'] || '';
    this.authService
      .login(this.username.trim(), this.password)
      .pipe(finalize(() => (this.busy = false)))
      .subscribe({
        next: () => {
          this.router.navigate([returnUrl]);
        },
        error: () => {
          this.loginError = true;
        },
      });
  }
}
