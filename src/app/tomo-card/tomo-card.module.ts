import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { TomoCardPageRoutingModule } from './tomo-card-routing.module';

import { TomoCardPage } from './tomo-card.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    TomoCardPageRoutingModule
  ],
  declarations: [TomoCardPage]
})
export class TomoCardPageModule {}
