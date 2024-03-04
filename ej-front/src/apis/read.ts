import service from "@/utils/request.js"

export function GetObj(updateParams){
    return service.request({
        method: "get",
        url: "/get_obj",
        params: updateParams
    })
}

export function PlusOne(updateParams){
    return service.request({
        method: "get",
        url: "/plus_one",
        params: updateParams
    })
}