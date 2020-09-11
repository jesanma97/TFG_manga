import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MiscoleccionesPage } from './miscolecciones.page';

const routes: Routes = [
  {
    path: '',
    component: MiscoleccionesPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MiscoleccionesPageRoutingModule {}
