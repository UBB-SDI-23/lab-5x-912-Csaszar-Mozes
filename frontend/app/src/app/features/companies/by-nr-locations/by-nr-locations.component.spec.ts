import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ByNrLocationsComponent } from './by-nr-locations.component';

describe('ByNrLocationsComponent', () => {
  let component: ByNrLocationsComponent;
  let fixture: ComponentFixture<ByNrLocationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ByNrLocationsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ByNrLocationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
