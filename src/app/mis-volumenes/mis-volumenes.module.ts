import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MisVolumenesPageRoutingModule } from './mis-volumenes-routing.module';

import { MisVolumenesPage } from './mis-volumenes.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MisVolumenesPageRoutingModule
  ],
  declarations: [MisVolumenesPage]
})
export class MisVolumenesPageModule {}
