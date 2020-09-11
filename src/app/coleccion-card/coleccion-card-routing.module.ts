import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ColeccionCardPage } from './coleccion-card.page';

const routes: Routes = [
  {
    path: '',
    component: ColeccionCardPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ColeccionCardPageRoutingModule {}
