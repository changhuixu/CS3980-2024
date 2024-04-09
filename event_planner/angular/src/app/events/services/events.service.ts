import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';
import { Event } from '../models/event';

@Injectable({ providedIn: 'root' })
export class EventsService {
  private readonly apiUrl = environment.apiUrl + `events`;
  constructor(private httpClient: HttpClient) {}

  getAllEvents(): Observable<Event[]> {
    return this.httpClient.get<Event[]>(this.apiUrl);
  }

  getEventDetails(id: string): Observable<Event> {
    return this.httpClient.get<Event>(`${this.apiUrl}/${id}`);
  }

  createEvent(
    title: string,
    image: string,
    description: string,
    tags: string[],
    location: string
  ): Observable<any> {
    return this.httpClient.post(`${this.apiUrl}/new`, {
      title,
      image,
      description,
      tags,
      location,
    });
  }

  updateEventDetails(
    id: string,
    title: string,
    image: string,
    description: string,
    tags: string[],
    location: string
  ): Observable<Event> {
    return this.httpClient.put<Event>(`${this.apiUrl}/${id}`, {
      title,
      image,
      description,
      tags,
      location,
    });
  }

  deleteEvent(id: string): Observable<any> {
    return this.httpClient.delete(`${this.apiUrl}/${id}`);
  }
}
