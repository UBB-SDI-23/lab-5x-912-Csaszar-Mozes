import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReputationGreaterThanComponent } from './reputation-greater-than.component';

describe('ReputationGreaterThanComponent', () => {
  let component: ReputationGreaterThanComponent;
  let fixture: ComponentFixture<ReputationGreaterThanComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ReputationGreaterThanComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReputationGreaterThanComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
