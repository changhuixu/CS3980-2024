import { inject } from '@angular/core';
import { Router, CanMatchFn, Route, UrlSegment } from '@angular/router';
import { AuthService } from '../services/auth.service';

export const authGuard: CanMatchFn = (route: Route, _: UrlSegment[]) => {
  const router = inject(Router);
  const authService = inject(AuthService);

  const navigation = router.getCurrentNavigation();

  const returnUrl = navigation?.extractedUrl.toString() || '/';

  const user = authService.user;
  if (user) {
    return true;
  } else {
    router.navigate(['login'], {
      queryParams: { returnUrl },
    });
    return false;
  }
};
