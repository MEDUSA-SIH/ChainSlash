import { jsx as _jsx, jsxs as _jsxs } from "react/jsx-runtime";
import AttributionPanel from '../components/AttributionPanel';
import FundFlowGraph from '../components/FundFlowGraph';
import CrossChainView from '../components/CrossChainView';
import CampaignView from '../components/CampaignView';
export default function Cases() {
    return (_jsxs("div", { children: [_jsx("h2", { children: "Cases (priority/status/chain/VASP/risk)" }), _jsx(AttributionPanel, {}), _jsx(FundFlowGraph, {}), _jsx(CrossChainView, {}), _jsx(CampaignView, {})] }));
}
