import { TestBed } from '@angular/core/testing';

import { ProveedorAPIService } from './proveedor-api.service';

describe('ProveedorAPIService', () => {
  let service: ProveedorAPIService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProveedorAPIService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
