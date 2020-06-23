import jsCookie from 'js-cookie'

import axios from 'axios'
axios.defaults.baseURL = 'http://127.0.0.1:8000';
//拦截请求
axios.interceptors.request.use(function (config) {
    // 在发起请求之前可以对请求进行处理 其中config就是请求中的config参数
	if(jsCookie.get('access')){
		config.headers.Authorization=`Bearer ${jsCookie.get('access')}`;
	}
    return config;
  }, function (error) {
    // Do something with request error
    return Promise.reject(error);
  });

//拦截响应
axios.interceptors.response.use(function (response) {
    // Do something with response data
    return response;
  }, function (error) {
    // Do something with response error
	if (error.response.status==401){
		console.log("认证失败")
		// 此处选择较为简单的直接重新登录,
		// 也可以根据refresh对access进行刷新 再次重新请求
		window.location.href="#/login";
		jsCookie.remove("access");
		jsCookie.remove("refresh");
		jsCookie.remove("username");
		jsCookie.remove("userinfo");
	}
    return Promise.reject(error);
  });
export const getCategoryList = ()=>{
	
	// 获取分类列表
	// this.$http({
				 //  method:'get',
				 //  url:'http://127.0.0.1:8000/api/v1/categorys/'
	// }).then(res=>{
				 //  console.log("得到分类列表",res);
	// }).catch(err=>{
				 //  console.log("发生错误",err);
	// })
	// 封装
	// return axios({
	// 	method:'get',
	// 	url:'/api/v1/categorys/'
	// })
	// 再封装
	return axios.get("/api/v1/categorys/")
	
	// console.log("getCategoryList执行了");
}

export const getCategoryDetail = (param)=>{
	return axios.get(`/api/v1/categorys/${param.id}/`)
} 

export const createCategory = (param)=>{
	// console.log("createCategory执行了",param);
	// 封装
	// return axios({
	// 	method:'post',
	// 	url:'/api/v1/categorys/',
	// 	data:param,
	// 	headers:{
	// 		Authorization:'Basic YWRtaW46MTIzNDU2'
	// 	}
		
	// })
	// 再封装
	return axios.post("/api/v1/categorys/",param,{
		// 通过配置请求的config 可不用下方的请求头信息
		// headers:{
		// 	Authorization:'Basic YWRtaW46MTIzNDU2'
		// }
	})
}

export const modifyCategory = (param)=>{
	return axios.put(`/api/v1/categorys/${param.id}/`,param,{
		// headers:{
		// 	Authorization:'Basic YWRtaW46MTIzNDU2'
		// }
	})
}

export const getToken = (param)=>{
	// console.log("getToken执行了",param);
	// 封装
	// return axios({
	// 	method:'post',
	// 	url:'/obtaintoken/',
	// 	data:param
	// })
	
	// 再封装
	return axios.post("/obtaintoken/",param,)
}
export const getUserInfo = (param)=>{
	return axios.get("/getuserinfo/",param,)
}

export const regist = (param)=>{
	return axios.post("/api/v1/users/",param,)
}

export const modifyUserInfo = (param)=>{
	// console.log("提交更改数据",param)
	let id = param.userinfo.id
	console.log("id为",id)
	return axios.patch(`/api/v1/users/${id}/`,param.userinfo,)
}

export const sendmsg = (param)=>{
	console.log("注册电话",param)
	return axios.post("/sendmsg/",param,)
}