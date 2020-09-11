import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ColeccionCardPage } from './coleccion-card.page';

describe('ColeccionCardPage', () => {
  let component: ColeccionCardPage;
  let fixture: ComponentFixture<ColeccionCardPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ColeccionCardPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ColeccionCardPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
