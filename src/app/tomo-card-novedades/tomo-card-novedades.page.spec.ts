import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { TomoCardNovedadesPage } from './tomo-card-novedades.page';

describe('TomoCardNovedadesPage', () => {
  let component: TomoCardNovedadesPage;
  let fixture: ComponentFixture<TomoCardNovedadesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TomoCardNovedadesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(TomoCardNovedadesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
