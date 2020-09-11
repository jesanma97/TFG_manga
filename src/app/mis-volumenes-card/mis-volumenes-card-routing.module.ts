import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { MisVolumenesCardPage } from './mis-volumenes-card.page';

const routes: Routes = [
  {
    path: '',
    component: MisVolumenesCardPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class MisVolumenesCardPageRoutingModule {}
