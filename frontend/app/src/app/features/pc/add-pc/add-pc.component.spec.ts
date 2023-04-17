import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddPcComponent } from './add-pc.component';

describe('AddPcComponent', () => {
  let component: AddPcComponent;
  let fixture: ComponentFixture<AddPcComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddPcComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddPcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
