export interface CameraProductPartMaterialInterface {
    id: number
    material: number
    image: string
}


export interface ProductPart {
    id: number,
    name: string,
    blender_name: string

}


export interface CameraProductPartInterface {
    part: ProductPart;
    materials: CameraProductPartMaterialInterface[]
}


export interface CameraInterface {
    parts: CameraProductPartInterface[]
    pos_x: number
    pos_y: number
    pos_z: number
    rad_x: number
    rad_y: number
    rad_z: number
}
