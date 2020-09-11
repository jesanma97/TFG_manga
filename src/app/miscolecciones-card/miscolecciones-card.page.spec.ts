import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MiscoleccionesCardPage } from './miscolecciones-card.page';

describe('MiscoleccionesCardPage', () => {
  let component: MiscoleccionesCardPage;
  let fixture: ComponentFixture<MiscoleccionesCardPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MiscoleccionesCardPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MiscoleccionesCardPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
