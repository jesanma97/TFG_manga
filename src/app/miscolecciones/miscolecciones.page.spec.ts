import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MiscoleccionesPage } from './miscolecciones.page';

describe('MiscoleccionesPage', () => {
  let component: MiscoleccionesPage;
  let fixture: ComponentFixture<MiscoleccionesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MiscoleccionesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MiscoleccionesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
