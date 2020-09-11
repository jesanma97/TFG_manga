import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MispendientesPage } from './mispendientes.page';

describe('MispendientesPage', () => {
  let component: MispendientesPage;
  let fixture: ComponentFixture<MispendientesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MispendientesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MispendientesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
