import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { MisVolumenesCardPageRoutingModule } from './mis-volumenes-card-routing.module';

import { MisVolumenesCardPage } from './mis-volumenes-card.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    MisVolumenesCardPageRoutingModule
  ],
  declarations: [MisVolumenesCardPage]
})
export class MisVolumenesCardPageModule {}
