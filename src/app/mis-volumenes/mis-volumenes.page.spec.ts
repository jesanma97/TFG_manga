import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { MisVolumenesPage } from './mis-volumenes.page';

describe('MisVolumenesPage', () => {
  let component: MisVolumenesPage;
  let fixture: ComponentFixture<MisVolumenesPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MisVolumenesPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(MisVolumenesPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
