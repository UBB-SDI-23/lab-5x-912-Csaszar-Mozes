import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GenerateDataComponent } from './generate-data.component';

describe('GenerateDataComponent', () => {
  let component: GenerateDataComponent;
  let fixture: ComponentFixture<GenerateDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GenerateDataComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(GenerateDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
