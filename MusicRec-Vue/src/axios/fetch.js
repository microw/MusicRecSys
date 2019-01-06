/**
 * Created by mingyue.yang on 2018/7/3.
 */
import axios from './axios'
import Vue from 'vue'
import qs from 'qs'

export default async(url = '', data = {}, type = 'GET', headers) => {

  type = type.toUpperCase();
  if (type == 'GET') {
    if (Object.keys(data).length !== 0) {
      url = url + '?' + qs.stringify(data);
    }
  }
  let requestConfig = {
    method: type,
    headers: headers || {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  if (type == 'POST') {
    requestConfig.data = qs.stringify(data);
  }
  const response = await axios(url, requestConfig);
  if (response) {
    return response.data;
  }
}
