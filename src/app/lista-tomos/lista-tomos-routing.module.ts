import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ListaTomosPage } from './lista-tomos.page';

const routes: Routes = [
  {
    path: '',
    component: ListaTomosPage
  },
  {
    path: 'lista-tomos',
    loadChildren: () => import('../lista-tomos/lista-tomos.module').then( m => m.ListaTomosPageModule)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ListaTomosPageRoutingModule {}
