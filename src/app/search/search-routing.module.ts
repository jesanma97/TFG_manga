import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { SearchPage } from './search.page';


const routes: Routes = [
  {
    path: '',
    component: SearchPage
  },{
    path:'coleccion-card',
    loadChildren: () => import('../coleccion-card/coleccion-card.module').then( m => m.ColeccionCardPageModule)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class SearchPageRoutingModule {}
