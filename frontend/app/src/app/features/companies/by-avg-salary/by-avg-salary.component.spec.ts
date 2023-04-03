import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ByAvgSalaryComponent } from './by-avg-salary.component';

describe('ByAvgSalaryComponent', () => {
  let component: ByAvgSalaryComponent;
  let fixture: ComponentFixture<ByAvgSalaryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ByAvgSalaryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ByAvgSalaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
