import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListAllPageComponent } from './list-all-page.component';
import { Company } from 'src/app/models/models';

describe('ListAllPageComponent', () => {
  let component: ListAllPageComponent;
  let fixture: ComponentFixture<ListAllPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListAllPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListAllPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
