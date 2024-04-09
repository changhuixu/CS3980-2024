import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { EventsRoutingModule } from './events-routing.module';
import { AllComponent } from './all/all.component';
import { DetailsComponent } from './details/details.component';
import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { SpinnerModule } from '@uiowa/spinner';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [AllComponent, DetailsComponent],
  imports: [
    CommonModule,
    EventsRoutingModule,
    FormsModule,
    NgbModalModule,
    SpinnerModule,
  ],
})
export class EventsModule {}
