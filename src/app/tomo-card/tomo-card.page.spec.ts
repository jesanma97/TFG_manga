import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { TomoCardPage } from './tomo-card.page';

describe('TomoCardPage', () => {
  let component: TomoCardPage;
  let fixture: ComponentFixture<TomoCardPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TomoCardPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(TomoCardPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
