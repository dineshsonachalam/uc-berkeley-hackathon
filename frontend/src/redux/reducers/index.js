// Step 3: Create reducers for the action types

import { combineReducers } from "redux";
import genderStatsReducer from "./genderStatsReducer";
export default combineReducers({ genderStatsReducer });