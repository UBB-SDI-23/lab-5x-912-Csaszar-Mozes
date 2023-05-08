import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SetPageSizeComponent } from './set-page-size.component';

describe('SetPageSizeComponent', () => {
  let component: SetPageSizeComponent;
  let fixture: ComponentFixture<SetPageSizeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SetPageSizeComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SetPageSizeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
