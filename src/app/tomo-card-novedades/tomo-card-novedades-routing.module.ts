import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { TomoCardNovedadesPage } from './tomo-card-novedades.page';

const routes: Routes = [
  {
    path: '',
    component: TomoCardNovedadesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class TomoCardNovedadesPageRoutingModule {}
