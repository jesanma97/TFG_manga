import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { ListaTomosPage } from './lista-tomos.page';

describe('ListaTomosPage', () => {
  let component: ListaTomosPage;
  let fixture: ComponentFixture<ListaTomosPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ListaTomosPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(ListaTomosPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
