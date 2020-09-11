import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { IntermediariaPage } from './intermediaria.page';

describe('IntermediariaPage', () => {
  let component: IntermediariaPage;
  let fixture: ComponentFixture<IntermediariaPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IntermediariaPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(IntermediariaPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
