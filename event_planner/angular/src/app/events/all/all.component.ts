import { Component, OnInit } from '@angular/core';
import { Event } from '../models/event';
import { EventsService } from '../services/events.service';
import { NgbModalRef, NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AuthService } from '../../core';
import { finalize } from 'rxjs';

@Component({
  selector: 'app-all',
  templateUrl: './all.component.html',
  styleUrl: './all.component.css',
})
export class AllComponent implements OnInit {
  events: Event[] = [];
  title = '';
  image = '';
  description = '';
  tags: string[] = [];
  location = '';
  busy = false;
  username = '';

  private modalRef?: NgbModalRef;
  constructor(
    authSvc: AuthService,
    private readonly svc: EventsService,
    private modalService: NgbModal
  ) {
    this.username = authSvc.user.username;
  }

  ngOnInit(): void {
    this.svc.getAllEvents().subscribe((x) => (this.events = x));
  }

  open(content: any) {
    this.modalRef = this.modalService.open(content, {
      size: 'lg',
      ariaLabelledBy: 'modal-title',
      backdrop: 'static',
    });
  }

  removeTag(t: string) {
    this.tags = this.tags.filter((x) => x !== t);
  }
  addTag(t: string) {
    if (t && !this.tags.includes(t)) {
      this.tags.push(t);
    }
  }

  create(content: any) {
    this.busy = true;
    this.svc
      .createEvent(
        this.title,
        this.image,
        this.description,
        this.tags,
        this.location
      )
      .pipe(finalize(() => (this.busy = false)))
      .subscribe((_) => {
        this.ngOnInit();
        this.modalRef?.close();
        this.open(content);
      });
  }

  delete(id: string) {
    this.svc.deleteEvent(id).subscribe((_) => {
      this.ngOnInit();
      this.modalRef?.close();
    });
  }
}
