import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MisVolumenesCardPage } from './mis-volumenes-card.page';

describe('MisVolumenesCardPage', () => {
  let component: MisVolumenesCardPage;
  let fixture: ComponentFixture<MisVolumenesCardPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MisVolumenesCardPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MisVolumenesCardPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
