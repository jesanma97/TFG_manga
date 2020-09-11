import { Component, OnInit } from '@angular/core';
import { ProveedorAPIService} from '../proveedor-api.service';
import { NavController } from '@ionic/angular';
import { FormControl } from '@angular/forms';
import {Router} from '@angular/router';


@Component({
  selector: 'app-search',
  templateUrl: './search.page.html',
  styleUrls: ['./search.page.scss'],
})
export class SearchPage {

  public datos_colec: any = [];
  public searchControl: FormControl;
  colecciones: any =[];
  inicio:any = [];
  public searchTerm: string = "";
  searching: any = false;
  public items: any;

  constructor(public router: Router,public navCtrl: NavController, public proveedor: ProveedorAPIService) { this.inicializaJSONData(); this.searchControl = new FormControl();}

 
  inicializaJSONData(){
    this.proveedor.obtenerDatosColecciones().subscribe((data)=>{this.colecciones = data;
    },
    (error)=>{console.log(error);})
  }

  filterItems(searchTerm){
    return this.colecciones.filter(item =>{
      return item.titulo.toLowerCase().indexOf(searchTerm.toLowerCase()) > -1;
    });
  }

  ngOnInit(){
    this.setFilteredItems();
    this.searchControl.valueChanges.subscribe(search =>{
      this.searching = false;
      this.searchTerm = search;
      this.setFilteredItems();
    });
  }


  onSearchInput(){
    this.searching = true;
  }

  setFilteredItems(){
    this.colecciones = this.filterItems(this.searchTerm);
  }

  public selectVal(item){
    this.router.navigate(['coleccion-card'],{queryParams:{valor:item}});
  }



}
