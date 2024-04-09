import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { authGuard } from './core';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { SignUpComponent } from './sign-up/sign-up.component';

const routes: Routes = [
  {
    path: '',
    pathMatch: 'full',
    component: HomeComponent,
    canMatch: [authGuard],
  },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignUpComponent },
  {
    path: 'events',
    loadChildren: () =>
      import('./events/events.module').then((m) => m.EventsModule),
    canMatch: [authGuard],
  },
  {
    path: 'management',
    loadChildren: () =>
      import('./management/management.module').then((m) => m.ManagementModule),
    canMatch: [authGuard],
  },
  { path: '**', redirectTo: '' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
