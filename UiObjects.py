import adsk.core, adsk.fusion, adsk.cam
__all__ = ['Toolbars', 'WorkSpaces', 'AllPanels', 'AllTabs']

class AllControls:
	class AlertCommand:
		ID = "AlertCommand"
		isNative = True
		class AlertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PerformanceFeedbackCommand:
		ID = "PerformanceFeedbackCommand"
		isNative = True
		class PerformanceFeedbackCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NotificationCenterCommand:
		ID = "NotificationCenterCommand"
		isNative = True
		class NotificationCenterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NotificationCommand:
		ID = "NotificationCommand"
		isNative = True
		class NotificationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CloudServiceStatusCommand:
		ID = "CloudServiceStatusCommand"
		isNative = True
	class GraphicsPerformanceMsgCommand:
		ID = "GraphicsPerformanceMsgCommand"
		isNative = True
		class GraphicsPerformanceMsgCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PlatformVerSupportDiscontinuedCommand:
		ID = "PlatformVerSupportDiscontinuedCommand"
		isNative = True
	class WhatsNewBanerCommand:
		ID = "WhatsNewBanerCommand"
		isNative = True
	class ReferralCommand:
		ID = "ReferralCommand"
		isNative = True
		class ReferralCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloudStatusCommand:
		ID = "CloudStatusCommand"
		isNative = True
		class CloudStatusCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FeaturePacksCommand:
		ID = "FeaturePacksCommand"
		isNative = True
		class FeaturePacksCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PreviewPacksCommand:
		ID = "PreviewPacksCommand"
		isNative = True
		class PreviewPacksCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ChatCommand:
		ID = "ChatCommand"
		isNative = True
		class ChatCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RemoveLinks:
		ID = "RemoveLinks"
		isNative = True
		class RemoveLinks_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AssetShellCommand:
		ID = "AssetShellCommand"
		isNative = True
		class AssetShellCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DashboardShellCommand:
		ID = "DashboardShellCommand"
		isNative = True
		class DashboardShellCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExitApplicationCommand:
		ID = "ExitApplicationCommand"
		isNative = True
		class ExitApplicationCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ClearUserCacheCommand:
		ID = "ClearUserCacheCommand"
		isNative = True
		class ClearUserCacheCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseAssetCommand:
		ID = "CloseAssetCommand"
		isNative = True
		class CloseAssetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PreviousAssetCommand:
		ID = "PreviousAssetCommand"
		isNative = True
		class PreviousAssetCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NextAssetCommand:
		ID = "NextAssetCommand"
		isNative = True
		class NextAssetCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SwitchAssetCommand:
		ID = "SwitchAssetCommand"
		isNative = True
		class SwitchAssetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InsertAssetCommand:
		ID = "InsertAssetCommand"
		isNative = True
	class ExportCommand:
		ID = "ExportCommand"
		isNative = True
		class ExportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CopyToDesktopCommand:
		ID = "CopyToDesktopCommand"
		isNative = True
		class CopyToDesktopCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SaveDocumentAsCommand:
		ID = "SaveDocumentAsCommand"
		isNative = True
		class SaveDocumentAsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SaveAsImageCommand:
		ID = "SaveAsImageCommand"
		isNative = True
		class SaveAsImageCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewDocumentCommand:
		ID = "NewDocumentCommand"
		isNative = True
		class NewDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewFromLocalCommand:
		ID = "NewFromLocalCommand"
		isNative = True
		class NewFromLocalCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewSingleDocumentCommand:
		ID = "NewSingleDocumentCommand"
		isNative = True
		class NewSingleDocumentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RenameCommand:
		ID = "RenameCommand"
		isNative = True
		class RenameCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenDocumentCommand:
		ID = "OpenDocumentCommand"
		isNative = True
		class OpenDocumentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SaveDocumentCommand:
		ID = "SaveDocumentCommand"
		isNative = True
		class SaveDocumentCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseDocumentCommand:
		ID = "CloseDocumentCommand"
		isNative = True
		class CloseDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseAllDocumentsCommand:
		ID = "CloseAllDocumentsCommand"
		isNative = True
		class CloseAllDocumentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CurrentlyOpenDocumentsCommand:
		ID = "CurrentlyOpenDocumentsCommand"
		isNative = True
	class RecentDocumentsCommand:
		ID = "RecentDocumentsCommand"
		isNative = True
	class CreateFromDesignCommand:
		ID = "CreateFromDesignCommand"
		isNative = True
		class CreateFromDesignCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ContinueDragFromDashboardCommand:
		ID = "ContinueDragFromDashboardCommand"
		isNative = True
		class ContinueDragFromDashboardCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360OpenAttachmentCommand:
		ID = "PLM360OpenAttachmentCommand"
		isNative = True
		class PLM360OpenAttachmentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360FileImportCommand:
		ID = "PLM360FileImportCommand"
		isNative = True
		class PLM360FileImportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AutoSaveFilesCommand:
		ID = "AutoSaveFilesCommand"
		isNative = True
		class AutoSaveFilesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360SaveCommand:
		ID = "PLM360SaveCommand"
		isNative = True
		class PLM360SaveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360SaveAsCommand:
		ID = "PLM360SaveAsCommand"
		isNative = True
		class PLM360SaveAsCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PLM360SaveNonFusionFileCommand:
		ID = "PLM360SaveNonFusionFileCommand"
		isNative = True
		class PLM360SaveNonFusionFileCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360NewItemCommand:
		ID = "PLM360NewItemCommand"
		isNative = True
		class PLM360NewItemCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360NotifyMessageCommand:
		ID = "PLM360NotifyMessageCommand"
		isNative = True
		class PLM360NotifyMessageCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360ExportFileCommand:
		ID = "PLM360ExportFileCommand"
		isNative = True
		class PLM360ExportFileCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360FileBrowserCommand:
		ID = "PLM360FileBrowserCommand"
		isNative = True
		class PLM360FileBrowserCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360LaunchStandaloneBrowser:
		ID = "PLM360LaunchStandaloneBrowser"
		isNative = True
		class PLM360LaunchStandaloneBrowser_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360OpenDetailsCommand:
		ID = "PLM360OpenDetailsCommand"
		isNative = True
		class PLM360OpenDetailsCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PLM360RefreshRenamedItemCommand:
		ID = "PLM360RefreshRenamedItemCommand"
		isNative = True
		class PLM360RefreshRenamedItemCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DashboardCreateMilestoneCommand:
		ID = "DashboardCreateMilestoneCommand"
		isNative = True
		class DashboardCreateMilestoneCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DashboardUpdateMilestoneCommand:
		ID = "DashboardUpdateMilestoneCommand"
		isNative = True
		class DashboardUpdateMilestoneCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FileSubMenuCommand:
		ID = "FileSubMenuCommand"
		isNative = True
		class FileSubMenuCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class F3ZFileImportCommand:
		ID = "F3ZFileImportCommand"
		isNative = True
		class F3ZFileImportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BranchingDialog:
		ID = "BranchingDialog"
		isNative = True
		class BranchingDialog_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowJobManagerDlgCmd:
		ID = "ShowJobManagerDlgCmd"
		isNative = True
		class ShowJobManagerDlgCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LearningPaletteCommand:
		ID = "LearningPaletteCommand"
		isNative = True
		class LearningPaletteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowLearningPaletteCommand:
		ID = "ShowLearningPaletteCommand"
		isNative = True
		class ShowLearningPaletteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideLearningPaletteCommand:
		ID = "HideLearningPaletteCommand"
		isNative = True
		class HideLearningPaletteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ScriptingDocumentationCommand:
		ID = "ScriptingDocumentationCommand"
		isNative = True
		class ScriptingDocumentationCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AboutBoxCommand:
		ID = "AboutBoxCommand"
		isNative = True
		class AboutBoxCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DemoControls2Command:
		ID = "DemoControls2Command"
		isNative = True
		class DemoControls2Command_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TestToolkitCommand:
		ID = "TestToolkitCommand"
		isNative = True
		class TestToolkitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TestOptionGroupCommand:
		ID = "TestOptionGroupCommand"
		isNative = True
		class TestOptionGroupCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TestTableCommand:
		ID = "TestTableCommand"
		isNative = True
		class TestTableCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TestTabBarCommand:
		ID = "TestTabBarCommand"
		isNative = True
		class TestTabBarCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowHUDCommand:
		ID = "ShowHUDCommand"
		isNative = True
		class ShowHUDCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GatherDiagnosticsDataCommand:
		ID = "GatherDiagnosticsDataCommand"
		isNative = True
		class GatherDiagnosticsDataCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CancelCommand:
		ID = "CancelCommand"
		isNative = True
		class CancelCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CommitCommand:
		ID = "CommitCommand"
		isNative = True
		class CommitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CutCommand:
		ID = "CutCommand"
		isNative = True
		class CutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DeleteCommand:
		ID = "DeleteCommand"
		isNative = True
		class DeleteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UndoCommand:
		ID = "UndoCommand"
		isNative = True
		class UndoCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RedoCommand:
		ID = "RedoCommand"
		isNative = True
		class RedoCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RepeatCommand:
		ID = "RepeatCommand"
		isNative = True
		class RepeatCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideTextCommandsCommand:
		ID = "HideTextCommandsCommand"
		isNative = True
		class HideTextCommandsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowTextCommandsCommand:
		ID = "ShowTextCommandsCommand"
		isNative = True
		class ShowTextCommandsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RunTestsCommand:
		ID = "RunTestsCommand"
		isNative = True
		class RunTestsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ProductTourGuideCommand:
		ID = "ProductTourGuideCommand"
		isNative = True
		class ProductTourGuideCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShareCommand:
		ID = "ShareCommand"
		isNative = True
		class ShareCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowNavigationToolbarCommand:
		ID = "ShowNavigationToolbarCommand"
		isNative = True
		class ShowNavigationToolbarCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideNavigationToolbarCommand:
		ID = "HideNavigationToolbarCommand"
		isNative = True
		class HideNavigationToolbarCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowBrowserCommand:
		ID = "ShowBrowserCommand"
		isNative = True
		class ShowBrowserCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideBrowserCommand:
		ID = "HideBrowserCommand"
		isNative = True
		class HideBrowserCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HelpGroupCommand:
		ID = "HelpGroupCommand"
		isNative = True
		class HelpGroupCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HelpCommand:
		ID = "HelpCommand"
		isNative = True
		class HelpCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LearningAndHelpCommand:
		ID = "LearningAndHelpCommand"
		isNative = True
		class LearningAndHelpCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CommunityCommand:
		ID = "CommunityCommand"
		isNative = True
		class CommunityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SupportAndDiagnosticsCommand:
		ID = "SupportAndDiagnosticsCommand"
		isNative = True
		class SupportAndDiagnosticsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LearningAndTutorialsCommand:
		ID = "LearningAndTutorialsCommand"
		isNative = True
		class LearningAndTutorialsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BlogCommand:
		ID = "BlogCommand"
		isNative = True
		class BlogCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class APIHelpCommand:
		ID = "APIHelpCommand"
		isNative = True
		class APIHelpCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SearchCommand:
		ID = "SearchCommand"
		isNative = True
	class ForumCommand:
		ID = "ForumCommand"
		isNative = True
		class ForumCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SubmitAnIdeaCommand:
		ID = "SubmitAnIdeaCommand"
		isNative = True
		class SubmitAnIdeaCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class StreetTeamCommand:
		ID = "StreetTeamCommand"
		isNative = True
		class StreetTeamCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ProductRoadmapCommand:
		ID = "ProductRoadmapCommand"
		isNative = True
		class ProductRoadmapCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WhatsNewCommand:
		ID = "WhatsNewCommand"
		isNative = True
		class WhatsNewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GalleryCommand:
		ID = "GalleryCommand"
		isNative = True
		class GalleryCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ExchangeAppStoreCommand:
		ID = "ExchangeAppStoreCommand"
		isNative = True
		class ExchangeAppStoreCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SubscriptionCommand:
		ID = "SubscriptionCommand"
		isNative = True
		class SubscriptionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CheckUpdatesCommand:
		ID = "CheckUpdatesCommand"
		isNative = True
		class CheckUpdatesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GraphicsDiagnosticsCommand:
		ID = "GraphicsDiagnosticsCommand"
		isNative = True
		class GraphicsDiagnosticsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class VideosCommand:
		ID = "VideosCommand"
		isNative = True
		class VideosCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FeedbackCommand:
		ID = "FeedbackCommand"
		isNative = True
		class FeedbackCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class THOAnalyticsCommand:
		ID = "THOAnalyticsCommand"
		isNative = True
		class THOAnalyticsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PreReleaseFeedbackCommand:
		ID = "PreReleaseFeedbackCommand"
		isNative = True
		class PreReleaseFeedbackCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class JoinDiscussionCommand:
		ID = "JoinDiscussionCommand"
		isNative = True
		class JoinDiscussionCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IdeaStationCommand:
		ID = "IdeaStationCommand"
		isNative = True
		class IdeaStationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class QuickStartCommand:
		ID = "QuickStartCommand"
		isNative = True
		class QuickStartCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TutorialsCommand:
		ID = "TutorialsCommand"
		isNative = True
		class TutorialsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MinimizeCommand:
		ID = "MinimizeCommand"
		isNative = True
		class MinimizeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ZoomWindowCommand:
		ID = "ZoomWindowCommand"
		isNative = True
		class ZoomWindowCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BringAllToFrontCommand:
		ID = "BringAllToFrontCommand"
		isNative = True
		class BringAllToFrontCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EnableAdaptiveSnapCmd:
		ID = "EnableAdaptiveSnapCmd"
		isNative = True
		class EnableAdaptiveSnapCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DisableAdaptiveSnapCmd:
		ID = "DisableAdaptiveSnapCmd"
		isNative = True
		class DisableAdaptiveSnapCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ToggleIncrementalMoveCmd:
		ID = "ToggleIncrementalMoveCmd"
		isNative = True
		class ToggleIncrementalMoveCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxControlDefinition"
	class SetSnapValueCmd:
		ID = "SetSnapValueCmd"
		isNative = True
		class SetSnapValueCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenWebBrowserCommand:
		ID = "OpenWebBrowserCommand"
		isNative = True
		class OpenWebBrowserCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ResetToDefaultLayoutCommand:
		ID = "ResetToDefaultLayoutCommand"
		isNative = True
		class ResetToDefaultLayoutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PreferencesCommand:
		ID = "PreferencesCommand"
		isNative = True
		class PreferencesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RunScriptCommand:
		ID = "RunScriptCommand"
		isNative = True
		class RunScriptCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ToolsCommand:
		ID = "ToolsCommand"
		isNative = True
		class ToolsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ScriptsManagerCommand:
		ID = "ScriptsManagerCommand"
		isNative = True
		class ScriptsManagerCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkOfflineCommand:
		ID = "WorkOfflineCommand"
		isNative = True
		class WorkOfflineCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UploadCommand:
		ID = "UploadCommand"
		isNative = True
		class UploadCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CollaborationMockDebugCmd:
		ID = "CollaborationMockDebugCmd"
		isNative = True
		class CollaborationMockDebugCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ZoomFitCommandGroup:
		ID = "ZoomFitCommandGroup"
		isNative = True
		class ZoomFitCommandGroup_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class OrbitCommand:
		ID = "OrbitCommand"
		isNative = True
		class OrbitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class FreeOrbitCommand:
		ID = "FreeOrbitCommand"
		isNative = True
		class FreeOrbitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConstrainedOrbitCommand:
		ID = "ConstrainedOrbitCommand"
		isNative = True
		class ConstrainedOrbitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ResetOrbitCenterCommand:
		ID = "ResetOrbitCenterCommand"
		isNative = True
		class ResetOrbitCenterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SetOrbitCenterCommand:
		ID = "SetOrbitCenterCommand"
		isNative = True
		class SetOrbitCenterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PowerAxisOrbitCommand:
		ID = "PowerAxisOrbitCommand"
		isNative = True
		class PowerAxisOrbitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TrackballOrbitCommand:
		ID = "TrackballOrbitCommand"
		isNative = True
		class TrackballOrbitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LookAtCommand:
		ID = "LookAtCommand"
		isNative = True
		class LookAtCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PanCommand:
		ID = "PanCommand"
		isNative = True
		class PanCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ZoomCommand:
		ID = "ZoomCommand"
		isNative = True
		class ZoomCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FitCommand:
		ID = "FitCommand"
		isNative = True
		class FitCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ZoomWindowViewCommand:
		ID = "ZoomWindowViewCommand"
		isNative = True
		class ZoomWindowViewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RotateCommand:
		ID = "RotateCommand"
		isNative = True
		class RotateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ViewsCommand:
		ID = "ViewsCommand"
		isNative = True
		class ViewsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectCommand:
		ID = "SelectCommand"
		isNative = True
		class SelectCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectionFilterCommand:
		ID = "SelectionFilterCommand"
		isNative = True
		class SelectionFilterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class EmptyInfo:
		ID = "EmptyInfo"
		isNative = True
		class EmptyInfo_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SelectFacePriorityCommand:
		ID = "SelectFacePriorityCommand"
		isNative = True
		class SelectFacePriorityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectBodyPriorityCommand:
		ID = "SelectBodyPriorityCommand"
		isNative = True
		class SelectBodyPriorityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectEdgePriorityCommand:
		ID = "SelectEdgePriorityCommand"
		isNative = True
		class SelectEdgePriorityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectComponentPriorityCommand:
		ID = "SelectComponentPriorityCommand"
		isNative = True
		class SelectComponentPriorityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectTSplineFacePriorityCommand:
		ID = "SelectTSplineFacePriorityCommand"
		isNative = True
		class SelectTSplineFacePriorityCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SelectTSplineBodyPriorityCommand:
		ID = "SelectTSplineBodyPriorityCommand"
		isNative = True
		class SelectTSplineBodyPriorityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectTSplineEdgePriorityCommand:
		ID = "SelectTSplineEdgePriorityCommand"
		isNative = True
		class SelectTSplineEdgePriorityCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ViewWidgetCommand:
		ID = "ViewWidgetCommand"
		isNative = True
		class ViewWidgetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowViewCubeCommand:
		ID = "ShowViewCubeCommand"
		isNative = True
		class ShowViewCubeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideViewCubeCommand:
		ID = "HideViewCubeCommand"
		isNative = True
		class HideViewCubeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FindInWindow:
		ID = "FindInWindow"
		isNative = True
		class FindInWindow_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FindInBrowser:
		ID = "FindInBrowser"
		isNative = True
		class FindInBrowser_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class VisibilityOverrideCommand:
		ID = "VisibilityOverrideCommand"
		isNative = True
		class VisibilityOverrideCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class GroundPlaneOffsetCommand:
		ID = "GroundPlaneOffsetCommand"
		isNative = True
		class GroundPlaneOffsetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseWorkspaceCommand:
		ID = "CloseWorkspaceCommand"
		isNative = True
		class CloseWorkspaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowWorkspaceFullScreenCommand:
		ID = "ShowWorkspaceFullScreenCommand"
		isNative = True
		class ShowWorkspaceFullScreenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowWorkspaceNormalCommand:
		ID = "ShowWorkspaceNormalCommand"
		isNative = True
		class ShowWorkspaceNormalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DashboardModeOpenCommand:
		ID = "DashboardModeOpenCommand"
		isNative = True
		class DashboardModeOpenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DashboardModeCloseCommand:
		ID = "DashboardModeCloseCommand"
		isNative = True
		class DashboardModeCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DashboardModeSwitchCommand:
		ID = "DashboardModeSwitchCommand"
		isNative = True
		class DashboardModeSwitchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ActivateProjectFilterCommand:
		ID = "ActivateProjectFilterCommand"
		isNative = True
		class ActivateProjectFilterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowActivityFeedCommand:
		ID = "ShowActivityFeedCommand"
		isNative = True
		class ShowActivityFeedCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideActivityFeedCommand:
		ID = "HideActivityFeedCommand"
		isNative = True
		class HideActivityFeedCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ActivateEnvironmentCommand:
		ID = "ActivateEnvironmentCommand"
		isNative = True
		class ActivateEnvironmentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class ReturnToEnvironmentCommand:
		ID = "ReturnToEnvironmentCommand"
		isNative = True
		class ReturnToEnvironmentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CycleWorkspacesForwardCommand:
		ID = "CycleWorkspacesForwardCommand"
		isNative = True
		class CycleWorkspacesForwardCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CycleWorkspacesBackwardCommand:
		ID = "CycleWorkspacesBackwardCommand"
		isNative = True
		class CycleWorkspacesBackwardCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class StartTranscriptingCommand:
		ID = "StartTranscriptingCommand"
		isNative = True
		class StartTranscriptingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class StartPerfTranscriptingCommand:
		ID = "StartPerfTranscriptingCommand"
		isNative = True
		class StartPerfTranscriptingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class StopTranscriptingCommand:
		ID = "StopTranscriptingCommand"
		isNative = True
		class StopTranscriptingCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReplayTranscriptCommand:
		ID = "ReplayTranscriptCommand"
		isNative = True
		class ReplayTranscriptCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ClearAllAlertsCommand:
		ID = "ClearAllAlertsCommand"
		isNative = True
		class ClearAllAlertsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowDebugDialogCommand:
		ID = "ShowDebugDialogCommand"
		isNative = True
		class ShowDebugDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideDebugDialogCommand:
		ID = "HideDebugDialogCommand"
		isNative = True
		class HideDebugDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowCommandPaletteCommand:
		ID = "ShowCommandPaletteCommand"
		isNative = True
		class ShowCommandPaletteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideCommandPaletteCommand:
		ID = "HideCommandPaletteCommand"
		isNative = True
		class HideCommandPaletteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DestroyDebugDialogCommand:
		ID = "DestroyDebugDialogCommand"
		isNative = True
		class DestroyDebugDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShareSheetsCommand:
		ID = "ShareSheetsCommand"
		isNative = True
	class ViewDisplayCommand:
		ID = "ViewDisplayCommand"
		isNative = True
		class ViewDisplayCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class ViewEffectCommand:
		ID = "ViewEffectCommand"
		isNative = True
		class ViewEffectCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class ViewDomeCommand:
		ID = "ViewDomeCommand"
		isNative = True
	class ViewGroundPlaneCommand:
		ID = "ViewGroundPlaneCommand"
		isNative = True
	class ViewGroundShadowCommand:
		ID = "ViewGroundShadowCommand"
		isNative = True
	class ViewGroundReflectionCommand:
		ID = "ViewGroundReflectionCommand"
		isNative = True
	class ViewAmbientOcclusionCommand:
		ID = "ViewAmbientOcclusionCommand"
		isNative = True
	class ViewNPREffectCommand:
		ID = "ViewNPREffectCommand"
		isNative = True
	class ViewEnvCommand:
		ID = "ViewEnvCommand"
		isNative = True
		class ViewEnvCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "RadioButtonListControlDefinition"
	class ViewMSAACommand:
		ID = "ViewMSAACommand"
		isNative = True
	class ViewSelectionEffectCommand:
		ID = "ViewSelectionEffectCommand"
		isNative = True
	class ViewVisualStyleCommand:
		ID = "ViewVisualStyleCommand"
		isNative = True
		class ViewVisualStyleCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "RadioButtonListControlDefinition"
	class ViewCameraCommand:
		ID = "ViewCameraCommand"
		isNative = True
		class ViewCameraCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "RadioButtonListControlDefinition"
	class ViewObjectShadowCommand:
		ID = "ViewObjectShadowCommand"
		isNative = True
	class ViewColorCyclingOnCmd:
		ID = "ViewColorCyclingOnCmd"
		isNative = True
		class ViewColorCyclingOnCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ViewColorCyclingOffCmd:
		ID = "ViewColorCyclingOffCmd"
		isNative = True
		class ViewColorCyclingOffCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ViewColorCyclingToggleCmd:
		ID = "ViewColorCyclingToggleCmd"
		isNative = True
		class ViewColorCyclingToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ViewLayoutGridOnCommand:
		ID = "ViewLayoutGridOnCommand"
		isNative = True
	class ViewLayoutGridLockCommand:
		ID = "ViewLayoutGridLockCommand"
		isNative = True
	class ToggleGridSnapCommand:
		ID = "ToggleGridSnapCommand"
		isNative = True
	class ViewLayoutGridCommand:
		ID = "ViewLayoutGridCommand"
		isNative = True
		class ViewLayoutGridCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class DefineGridCmd:
		ID = "DefineGridCmd"
		isNative = True
		class DefineGridCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InCanvasRenderCommand:
		ID = "InCanvasRenderCommand"
		isNative = True
		class InCanvasRenderCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InCanvasRenderSettingsCommand:
		ID = "InCanvasRenderSettingsCommand"
		isNative = True
		class InCanvasRenderSettingsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SplitViewWindowSyncCommand:
		ID = "SplitViewWindowSyncCommand"
		isNative = True
		class SplitViewWindowSyncCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class SplitViewWindowSyncOnCommand:
		ID = "SplitViewWindowSyncOnCommand"
		isNative = True
		class SplitViewWindowSyncOnCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SplitViewCommand:
		ID = "SplitViewCommand"
		isNative = True
	class SingleViewCmd:
		ID = "SingleViewCmd"
		isNative = True
	class MultiViewCmd:
		ID = "MultiViewCmd"
		isNative = True
	class SplitViewResetCmd:
		ID = "SplitViewResetCmd"
		isNative = True
	class SplitViewVisualStyleCommand:
		ID = "SplitViewVisualStyleCommand"
		isNative = True
		class SplitViewVisualStyleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "RadioButtonListControlDefinition"
	class SplitViewCameraCommand:
		ID = "SplitViewCameraCommand"
		isNative = True
		class SplitViewCameraCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "RadioButtonListControlDefinition"
	class AddNamedViewCommand:
		ID = "AddNamedViewCommand"
		isNative = True
		class AddNamedViewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RemoveNamedViewCommand:
		ID = "RemoveNamedViewCommand"
		isNative = True
		class RemoveNamedViewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateNamedViewCameraCommand:
		ID = "UpdateNamedViewCameraCommand"
		isNative = True
		class UpdateNamedViewCameraCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateNamedViewNameCommand:
		ID = "UpdateNamedViewNameCommand"
		isNative = True
		class UpdateNamedViewNameCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RestoreCameraCommand:
		ID = "RestoreCameraCommand"
		isNative = True
		class RestoreCameraCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NotifyAutoSaveFilesCommand:
		ID = "NotifyAutoSaveFilesCommand"
		isNative = True
		class NotifyAutoSaveFilesCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HomeCommand:
		ID = "HomeCommand"
		isNative = True
		class HomeCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GoBackwardCommand:
		ID = "GoBackwardCommand"
		isNative = True
		class GoBackwardCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GoForwardCommand:
		ID = "GoForwardCommand"
		isNative = True
		class GoForwardCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RefreshCommand:
		ID = "RefreshCommand"
		isNative = True
		class RefreshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UserDisplayNameCommand:
		ID = "UserDisplayNameCommand"
		isNative = True
		class UserDisplayNameCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CurrentlyOpenPagesCommand:
		ID = "CurrentlyOpenPagesCommand"
		isNative = True
		class CurrentlyOpenPagesCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseAllDocumentTabsCommand:
		ID = "CloseAllDocumentTabsCommand"
		isNative = True
		class CloseAllDocumentTabsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseDocumentTabCommand:
		ID = "CloseDocumentTabCommand"
		isNative = True
		class CloseDocumentTabCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CycleTabsForwardCommand:
		ID = "CycleTabsForwardCommand"
		isNative = True
		class CycleTabsForwardCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CycleTabsBackwardCommand:
		ID = "CycleTabsBackwardCommand"
		isNative = True
		class CycleTabsBackwardCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GoToMyProfileCommand:
		ID = "GoToMyProfileCommand"
		isNative = True
		class GoToMyProfileCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GoToMyAccountCommand:
		ID = "GoToMyAccountCommand"
		isNative = True
		class GoToMyAccountCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SubscribeNowCommand:
		ID = "SubscribeNowCommand"
		isNative = True
		class SubscribeNowCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MyCloudCommand:
		ID = "MyCloudCommand"
		isNative = True
		class MyCloudCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UserHubsCommand:
		ID = "UserHubsCommand"
		isNative = True
		class UserHubsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class JoinTeamCommand:
		ID = "JoinTeamCommand"
		isNative = True
		class JoinTeamCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OldUserToTeamFromInviteCommand:
		ID = "OldUserToTeamFromInviteCommand"
		isNative = True
		class OldUserToTeamFromInviteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class QontextLogoutCommand:
		ID = "QontextLogoutCommand"
		isNative = True
		class QontextLogoutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CloseAllDocumentsAndLogoutCommand:
		ID = "CloseAllDocumentsAndLogoutCommand"
		isNative = True
		class CloseAllDocumentsAndLogoutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TryToBuyCommand:
		ID = "TryToBuyCommand"
		isNative = True
		class TryToBuyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PurchasePackCommand:
		ID = "PurchasePackCommand"
		isNative = True
		class PurchasePackCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExtensionTrialCommand:
		ID = "ExtensionTrialCommand"
		isNative = True
		class ExtensionTrialCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AutoLoginCommand:
		ID = "AutoLoginCommand"
		isNative = True
		class AutoLoginCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HealthStatusCommand:
		ID = "HealthStatusCommand"
		isNative = True
		class HealthStatusCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class BasicAccessCommand:
		ID = "BasicAccessCommand"
		isNative = True
		class BasicAccessCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CapacityLimitStatusCommand:
		ID = "CapacityLimitStatusCommand"
		isNative = True
		class CapacityLimitStatusCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimpleSharingPublicLinkCommand:
		ID = "SimpleSharingPublicLinkCommand"
		isNative = True
		class SimpleSharingPublicLinkCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class A360RenderCommand:
		ID = "A360RenderCommand"
		isNative = True
		class A360RenderCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class A360RenderGalleryCommand:
		ID = "A360RenderGalleryCommand"
		isNative = True
		class A360RenderGalleryCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LiveReviewCommand:
		ID = "LiveReviewCommand"
		isNative = True
		class LiveReviewCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CopyDocumentsCommand:
		ID = "CopyDocumentsCommand"
		isNative = True
		class CopyDocumentsCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MoveDocumentsCommand:
		ID = "MoveDocumentsCommand"
		isNative = True
		class MoveDocumentsCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TransferToTeamHubCommand:
		ID = "TransferToTeamHubCommand"
		isNative = True
		class TransferToTeamHubCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MarkDocumentsForOpenCommand:
		ID = "MarkDocumentsForOpenCommand"
		isNative = True
		class MarkDocumentsForOpenCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateRelatedItemsCommand:
		ID = "UpdateRelatedItemsCommand"
		isNative = True
		class UpdateRelatedItemsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HistoryCommand:
		ID = "HistoryCommand"
		isNative = True
		class HistoryCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TeamSwitcherCommand:
		ID = "TeamSwitcherCommand"
		isNative = True
		class TeamSwitcherCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LearningPanelCloseCommand:
		ID = "LearningPanelCloseCommand"
		isNative = True
		class LearningPanelCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LearningPanelOpenCommand:
		ID = "LearningPanelOpenCommand"
		isNative = True
		class LearningPanelOpenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MoreHelpCommand:
		ID = "MoreHelpCommand"
		isNative = True
		class MoreHelpCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ActiveDocumentActivateCommand:
		ID = "ActiveDocumentActivateCommand"
		isNative = True
		class ActiveDocumentActivateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActiveDocumentDeactivateCommand:
		ID = "ActiveDocumentDeactivateCommand"
		isNative = True
		class ActiveDocumentDeactivateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActiveDocumentsShowActiveDocumentsListCommand:
		ID = "ActiveDocumentsShowActiveDocumentsListCommand"
		isNative = True
		class ActiveDocumentsShowActiveDocumentsListCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActiveDocumentsLearnMoreBasicAccessCommand:
		ID = "ActiveDocumentsLearnMoreBasicAccessCommand"
		isNative = True
		class ActiveDocumentsLearnMoreBasicAccessCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RestrictedUserCommand:
		ID = "RestrictedUserCommand"
		isNative = True
		class RestrictedUserCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LoadInHomeTabCommand:
		ID = "LoadInHomeTabCommand"
		isNative = True
		class LoadInHomeTabCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShareFeedbackCommand:
		ID = "ShareFeedbackCommand"
		isNative = True
		class ShareFeedbackCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NTestExcCommand:
		ID = "NTestExcCommand"
		isNative = True
		class NTestExcCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UndoDropDown:
		ID = "UndoDropDown"
		isNative = True
		class UndoDropDown_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class RedoDropDown:
		ID = "RedoDropDown"
		isNative = True
		class RedoDropDown_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class CopyCommand:
		ID = "CopyCommand"
		isNative = True
		class CopyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PasteCommand:
		ID = "PasteCommand"
		isNative = True
		class PasteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SaveAsSATCommand:
		ID = "SaveAsSATCommand"
		isNative = True
		class SaveAsSATCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SaveAsASMCommand:
		ID = "SaveAsASMCommand"
		isNative = True
		class SaveAsASMCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MaterialCommand:
		ID = "MaterialCommand"
		isNative = True
		class MaterialCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PhysicalMaterialEditOnlyCommand:
		ID = "PhysicalMaterialEditOnlyCommand"
		isNative = True
		class PhysicalMaterialEditOnlyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SuppressAppearanceCmd:
		ID = "SuppressAppearanceCmd"
		isNative = True
	class RemoveOverrideCommand:
		ID = "RemoveOverrideCommand"
		isNative = True
		class RemoveOverrideCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowAffectedFacesCommand:
		ID = "ShowAffectedFacesCommand"
		isNative = True
		class ShowAffectedFacesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DataBrowserCommand:
		ID = "DataBrowserCommand"
		isNative = True
		class DataBrowserCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DumpEntityCommand:
		ID = "DumpEntityCommand"
		isNative = True
		class DumpEntityCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SanityCheckCommand:
		ID = "SanityCheckCommand"
		isNative = True
		class SanityCheckCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ASMDebugOptionsCommand:
		ID = "ASMDebugOptionsCommand"
		isNative = True
		class ASMDebugOptionsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ASMDebugChecksCommand:
		ID = "ASMDebugChecksCommand"
		isNative = True
		class ASMDebugChecksCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EntityFinderCommand:
		ID = "EntityFinderCommand"
		isNative = True
		class EntityFinderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class VisibilityToggleCmd:
		ID = "VisibilityToggleCmd"
		isNative = True
		class VisibilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowAllComponentsCmd:
		ID = "ShowAllComponentsCmd"
		isNative = True
		class ShowAllComponentsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowAllBodiesCmd:
		ID = "ShowAllBodiesCmd"
		isNative = True
		class ShowAllBodiesCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectabilityToggleCmd:
		ID = "SelectabilityToggleCmd"
		isNative = True
		class SelectabilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PlanesVisibilityToggleCmd:
		ID = "PlanesVisibilityToggleCmd"
		isNative = True
		class PlanesVisibilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AxesVisibilityToggleCmd:
		ID = "AxesVisibilityToggleCmd"
		isNative = True
		class AxesVisibilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PointsVisibilityToggleCmd:
		ID = "PointsVisibilityToggleCmd"
		isNative = True
		class PointsVisibilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PythonInteractiveCommand:
		ID = "PythonInteractiveCommand"
		isNative = True
		class PythonInteractiveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PythonSequentialCommand:
		ID = "PythonSequentialCommand"
		isNative = True
		class PythonSequentialCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CommentObjectCommand:
		ID = "CommentObjectCommand"
		isNative = True
		class CommentObjectCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ViewCommentCmd:
		ID = "ViewCommentCmd"
		isNative = True
		class ViewCommentCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeasureCommand:
		ID = "MeasureCommand"
		isNative = True
		class MeasureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CycleComponentColorCmd:
		ID = "CycleComponentColorCmd"
		isNative = True
		class CycleComponentColorCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RemoveVisibilityOverridesCommand:
		ID = "RemoveVisibilityOverridesCommand"
		isNative = True
		class RemoveVisibilityOverridesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CreateSelectionGroupCmd:
		ID = "CreateSelectionGroupCmd"
		isNative = True
		class CreateSelectionGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectSelectionGroupCmd:
		ID = "SelectSelectionGroupCmd"
		isNative = True
		class SelectSelectionGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateSelectionGroupCmd:
		ID = "UpdateSelectionGroupCmd"
		isNative = True
		class UpdateSelectionGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GhostedBodyToggleCommand:
		ID = "GhostedBodyToggleCommand"
		isNative = True
		class GhostedBodyToggleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionImportCommand:
		ID = "FusionImportCommand"
		isNative = True
		class FusionImportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionImportFromLocalCommand:
		ID = "FusionImportFromLocalCommand"
		isNative = True
		class FusionImportFromLocalCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeActiveUnitsCommand:
		ID = "FusionChangeActiveUnitsCommand"
		isNative = True
		class FusionChangeActiveUnitsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeActiveUnitsInternalCommand:
		ID = "FusionChangeActiveUnitsInternalCommand"
		isNative = True
		class FusionChangeActiveUnitsInternalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PIMAssignItemNumberCmd:
		ID = "PIMAssignItemNumberCmd"
		isNative = True
		class PIMAssignItemNumberCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PIMQuickReleaseCmd:
		ID = "PIMQuickReleaseCmd"
		isNative = True
		class PIMQuickReleaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PIMECOReleaseCmd:
		ID = "PIMECOReleaseCmd"
		isNative = True
		class PIMECOReleaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ChangeThreadTypeCommand:
		ID = "ChangeThreadTypeCommand"
		isNative = True
		class ChangeThreadTypeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDeleteCommand:
		ID = "FusionDeleteCommand"
		isNative = True
		class FusionDeleteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RenderingEnvCmd:
		ID = "RenderingEnvCmd"
		isNative = True
		class RenderingEnvCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AppearanceCommand:
		ID = "AppearanceCommand"
		isNative = True
		class AppearanceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PhysicalMaterialCommand:
		ID = "PhysicalMaterialCommand"
		isNative = True
		class PhysicalMaterialCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveOverrideCommand:
		ID = "FusionRemoveOverrideCommand"
		isNative = True
		class FusionRemoveOverrideCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReturnToExternalAppCmdDefINV:
		ID = "ReturnToExternalAppCmdDefINV"
		isNative = True
		class ReturnToExternalAppCmdDefINV_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReturnToExternalAppCmdDefACAD:
		ID = "ReturnToExternalAppCmdDefACAD"
		isNative = True
		class ReturnToExternalAppCmdDefACAD_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReturnToExternalAppCmdDefMoldflow:
		ID = "ReturnToExternalAppCmdDefMoldflow"
		isNative = True
		class ReturnToExternalAppCmdDefMoldflow_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionOffsetFacesCommand:
		ID = "FusionOffsetFacesCommand"
		isNative = True
		class FusionOffsetFacesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionFilletEdgesCommand:
		ID = "FusionFilletEdgesCommand"
		isNative = True
		class FusionFilletEdgesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionGapFillCommand:
		ID = "FusionGapFillCommand"
		isNative = True
		class FusionGapFillCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DCFusionGapFillEditCmd:
		ID = "DCFusionGapFillEditCmd"
		isNative = True
		class DCFusionGapFillEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionFilletEditCommand:
		ID = "FusionFilletEditCommand"
		isNative = True
		class FusionFilletEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionHoleCommand:
		ID = "FusionHoleCommand"
		isNative = True
		class FusionHoleCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionHoleEditCommand:
		ID = "FusionHoleEditCommand"
		isNative = True
		class FusionHoleEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcHoleEditCommand:
		ID = "FusionDcHoleEditCommand"
		isNative = True
		class FusionDcHoleEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionThreadCommand:
		ID = "FusionThreadCommand"
		isNative = True
		class FusionThreadCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionThreadEditCommand:
		ID = "FusionThreadEditCommand"
		isNative = True
		class FusionThreadEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcThreadEditCommand:
		ID = "FusionDcThreadEditCommand"
		isNative = True
		class FusionDcThreadEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChamferCommand:
		ID = "FusionChamferCommand"
		isNative = True
		class FusionChamferCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionChamferEditCommand:
		ID = "FusionChamferEditCommand"
		isNative = True
		class FusionChamferEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDeleteFacesCommand:
		ID = "FusionDeleteFacesCommand"
		isNative = True
		class FusionDeleteFacesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcDeleteFaceEditCommand:
		ID = "FusionDcDeleteFaceEditCommand"
		isNative = True
		class FusionDcDeleteFaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionReplaceFaceCommand:
		ID = "FusionReplaceFaceCommand"
		isNative = True
		class FusionReplaceFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EmbossCmd:
		ID = "EmbossCmd"
		isNative = True
		class EmbossCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEmbossEditCmd:
		ID = "FusionDcEmbossEditCmd"
		isNative = True
		class FusionDcEmbossEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcReplaceFaceEditCommand:
		ID = "FusionDcReplaceFaceEditCommand"
		isNative = True
		class FusionDcReplaceFaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionShellBodyCommand:
		ID = "FusionShellBodyCommand"
		isNative = True
		class FusionShellBodyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShellManagerCommand:
		ID = "ShellManagerCommand"
		isNative = True
		class ShellManagerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcShellFeatureEditCommand:
		ID = "FusionDcShellFeatureEditCommand"
		isNative = True
		class FusionDcShellFeatureEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionMoveComponentsCommand:
		ID = "FusionMoveComponentsCommand"
		isNative = True
		class FusionMoveComponentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMoveCommand:
		ID = "FusionMoveCommand"
		isNative = True
		class FusionMoveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcMoveBodyEditCommand:
		ID = "FusionDcMoveBodyEditCommand"
		isNative = True
		class FusionDcMoveBodyEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcMoveCopyEditCommand:
		ID = "FusionDcMoveCopyEditCommand"
		isNative = True
		class FusionDcMoveCopyEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcAlignEditCommand:
		ID = "FusionDcAlignEditCommand"
		isNative = True
		class FusionDcAlignEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionMoveJointsCommand:
		ID = "FusionMoveJointsCommand"
		isNative = True
		class FusionMoveJointsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AlignComponentsCmd:
		ID = "AlignComponentsCmd"
		isNative = True
		class AlignComponentsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AlignGeometryCmd:
		ID = "AlignGeometryCmd"
		isNative = True
		class AlignGeometryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AlignCmd:
		ID = "AlignCmd"
		isNative = True
		class AlignCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SuppressJointOccurrenceCmd:
		ID = "SuppressJointOccurrenceCmd"
		isNative = True
		class SuppressJointOccurrenceCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnsuppressJointOccurrenceCmd:
		ID = "UnsuppressJointOccurrenceCmd"
		isNative = True
		class UnsuppressJointOccurrenceCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SuppressRigidGroupCmd:
		ID = "SuppressRigidGroupCmd"
		isNative = True
		class SuppressRigidGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnsuppressRigidGroupCmd:
		ID = "UnsuppressRigidGroupCmd"
		isNative = True
		class UnsuppressRigidGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SuppressMotionRelationshipCmd:
		ID = "SuppressMotionRelationshipCmd"
		isNative = True
		class SuppressMotionRelationshipCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnsuppressMotionRelationshipCmd:
		ID = "UnsuppressMotionRelationshipCmd"
		isNative = True
		class UnsuppressMotionRelationshipCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ContactSetCmd:
		ID = "ContactSetCmd"
		isNative = True
		class ContactSetCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditContactSetCmd:
		ID = "EditContactSetCmd"
		isNative = True
		class EditContactSetCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SuppressContactSetCmd:
		ID = "SuppressContactSetCmd"
		isNative = True
		class SuppressContactSetCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnsuppressContactSetCmd:
		ID = "UnsuppressContactSetCmd"
		isNative = True
		class UnsuppressContactSetCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EnableContactSetsCmd:
		ID = "EnableContactSetsCmd"
		isNative = True
		class EnableContactSetsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EnableAllContactCmd:
		ID = "EnableAllContactCmd"
		isNative = True
		class EnableAllContactCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DisableAllContactCmd:
		ID = "DisableAllContactCmd"
		isNative = True
		class DisableAllContactCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LockJointCmd:
		ID = "LockJointCmd"
		isNative = True
		class LockJointCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnlockJointCmd:
		ID = "UnlockJointCmd"
		isNative = True
		class UnlockJointCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AnimateJointCmd:
		ID = "AnimateJointCmd"
		isNative = True
		class AnimateJointCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AnimateModelCmd:
		ID = "AnimateModelCmd"
		isNative = True
		class AnimateModelCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RestoreJointCmd:
		ID = "RestoreJointCmd"
		isNative = True
		class RestoreJointCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMotionStudyCommand:
		ID = "FusionMotionStudyCommand"
		isNative = True
		class FusionMotionStudyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditMotionStudyCmd:
		ID = "EditMotionStudyCmd"
		isNative = True
		class EditMotionStudyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectJointComponentsCmd:
		ID = "SelectJointComponentsCmd"
		isNative = True
		class SelectJointComponentsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectJointsByComponentCmd:
		ID = "SelectJointsByComponentCmd"
		isNative = True
		class SelectJointsByComponentCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectMotionLinkJointsCmd:
		ID = "SelectMotionLinkJointsCmd"
		isNative = True
		class SelectMotionLinkJointsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RedefineJointHomeCmd:
		ID = "RedefineJointHomeCmd"
		isNative = True
		class RedefineJointHomeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDragComponentsCommand:
		ID = "FusionDragComponentsCommand"
		isNative = True
		class FusionDragComponentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDragCompControlsCmd:
		ID = "FusionDragCompControlsCmd"
		isNative = True
		class FusionDragCompControlsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionShowSelectionPanelCmd:
		ID = "FusionShowSelectionPanelCmd"
		isNative = True
		class FusionShowSelectionPanelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDragJointOriginCommand:
		ID = "FusionDragJointOriginCommand"
		isNative = True
		class FusionDragJointOriginCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionGroundComponentsCommand:
		ID = "FusionGroundComponentsCommand"
		isNative = True
		class FusionGroundComponentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionUnGroundComponentsCommand:
		ID = "FusionUnGroundComponentsCommand"
		isNative = True
		class FusionUnGroundComponentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionUpdateCommand:
		ID = "FusionUpdateCommand"
		isNative = True
		class FusionUpdateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMultiSelInputTestCmd:
		ID = "FusionMultiSelInputTestCmd"
		isNative = True
		class FusionMultiSelInputTestCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ModifyScale:
		ID = "ModifyScale"
		isNative = True
		class ModifyScale_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CmdPreviewGraphicsTestCommand:
		ID = "CmdPreviewGraphicsTestCommand"
		isNative = True
		class CmdPreviewGraphicsTestCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InterferenceCheckCommand:
		ID = "InterferenceCheckCommand"
		isNative = True
		class InterferenceCheckCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcScaleEditCommand:
		ID = "FusionDcScaleEditCommand"
		isNative = True
		class FusionDcScaleEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IsolateCmd:
		ID = "IsolateCmd"
		isNative = True
		class IsolateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnisolateCmd:
		ID = "UnisolateCmd"
		isNative = True
		class UnisolateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnisolateAllCmd:
		ID = "UnisolateAllCmd"
		isNative = True
		class UnisolateAllCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchCreate:
		ID = "SketchCreate"
		isNative = True
		class SketchCreate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchStop:
		ID = "SketchStop"
		isNative = True
		class SketchStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchActivate:
		ID = "SketchActivate"
		isNative = True
		class SketchActivate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ProfileSketchActivate:
		ID = "ProfileSketchActivate"
		isNative = True
		class ProfileSketchActivate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SaveSketchAsDWG:
		ID = "SaveSketchAsDWG"
		isNative = True
		class SaveSketchAsDWG_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DrawPolyline:
		ID = "DrawPolyline"
		isNative = True
		class DrawPolyline_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceThickenCommand:
		ID = "FusionSurfaceThickenCommand"
		isNative = True
		class FusionSurfaceThickenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDraftCommand:
		ID = "FusionDraftCommand"
		isNative = True
		class FusionDraftCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCombineCommand:
		ID = "FusionCombineCommand"
		isNative = True
		class FusionCombineCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCombineEditCommand:
		ID = "FusionCombineEditCommand"
		isNative = True
		class FusionCombineEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSplitBodyCommand:
		ID = "FusionSplitBodyCommand"
		isNative = True
		class FusionSplitBodyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSplitBodyEditCommand:
		ID = "FusionDcSplitBodyEditCommand"
		isNative = True
		class FusionDcSplitBodyEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcPartingLineSplitEditCommand:
		ID = "FusionDcPartingLineSplitEditCommand"
		isNative = True
		class FusionDcPartingLineSplitEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSplitFaceEditCommand:
		ID = "FusionDcSplitFaceEditCommand"
		isNative = True
		class FusionDcSplitFaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSplitFaceCommand:
		ID = "FusionSplitFaceCommand"
		isNative = True
		class FusionSplitFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionPartingLineSplitCmd:
		ID = "FusionPartingLineSplitCmd"
		isNative = True
		class FusionPartingLineSplitCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class Extrude:
		ID = "Extrude"
		isNative = True
		class Extrude_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionExtrudeEditCommand:
		ID = "FusionExtrudeEditCommand"
		isNative = True
		class FusionExtrudeEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Revolve:
		ID = "Revolve"
		isNative = True
		class Revolve_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TextureMappingCommand:
		ID = "TextureMappingCommand"
		isNative = True
		class TextureMappingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionRevolveEditCommand:
		ID = "FusionRevolveEditCommand"
		isNative = True
		class FusionRevolveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceRevolveEditCommand:
		ID = "FusionSurfaceRevolveEditCommand"
		isNative = True
		class FusionSurfaceRevolveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Sweep:
		ID = "Sweep"
		isNative = True
		class Sweep_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSweepEditCommand:
		ID = "FusionSweepEditCommand"
		isNative = True
		class FusionSweepEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceSweepEditCommand:
		ID = "FusionSurfaceSweepEditCommand"
		isNative = True
		class FusionSurfaceSweepEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SolidLoft:
		ID = "SolidLoft"
		isNative = True
		class SolidLoft_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionLoftEditCommand:
		ID = "FusionLoftEditCommand"
		isNative = True
		class FusionLoftEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineLoft:
		ID = "TSplineLoft"
		isNative = True
		class TSplineLoft_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRibCommand:
		ID = "FusionRibCommand"
		isNative = True
		class FusionRibCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcRibEditCommand:
		ID = "FusionDcRibEditCommand"
		isNative = True
		class FusionDcRibEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionWebCommand:
		ID = "FusionWebCommand"
		isNative = True
		class FusionWebCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcWebEditCommand:
		ID = "FusionDcWebEditCommand"
		isNative = True
		class FusionDcWebEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfaceSculpt:
		ID = "SurfaceSculpt"
		isNative = True
		class SurfaceSculpt_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSculptEditCommand:
		ID = "FusionSculptEditCommand"
		isNative = True
		class FusionSculptEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfaceLoft:
		ID = "SurfaceLoft"
		isNative = True
		class SurfaceLoft_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceLoftEditCommand:
		ID = "FusionSurfaceLoftEditCommand"
		isNative = True
		class FusionSurfaceLoftEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitiveBox:
		ID = "PrimitiveBox"
		isNative = True
		class PrimitiveBox_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BoxPrimitiveEditCommand:
		ID = "BoxPrimitiveEditCommand"
		isNative = True
		class BoxPrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitiveBox:
		ID = "SurfPrimitiveBox"
		isNative = True
		class SurfPrimitiveBox_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitiveCylinder:
		ID = "PrimitiveCylinder"
		isNative = True
		class PrimitiveCylinder_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CylinderPrimitiveEditCommand:
		ID = "CylinderPrimitiveEditCommand"
		isNative = True
		class CylinderPrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitiveCylinder:
		ID = "SurfPrimitiveCylinder"
		isNative = True
		class SurfPrimitiveCylinder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitiveSphere:
		ID = "PrimitiveSphere"
		isNative = True
		class PrimitiveSphere_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SpherePrimitiveEditCommand:
		ID = "SpherePrimitiveEditCommand"
		isNative = True
		class SpherePrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CoilPrimitiveEditCommand:
		ID = "CoilPrimitiveEditCommand"
		isNative = True
		class CoilPrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitiveSphere:
		ID = "SurfPrimitiveSphere"
		isNative = True
		class SurfPrimitiveSphere_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitiveTorus:
		ID = "PrimitiveTorus"
		isNative = True
		class PrimitiveTorus_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TorusPrimitiveEditCommand:
		ID = "TorusPrimitiveEditCommand"
		isNative = True
		class TorusPrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Torus:
		ID = "Torus"
		isNative = True
		class Torus_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitiveTorus:
		ID = "SurfPrimitiveTorus"
		isNative = True
		class SurfPrimitiveTorus_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfTorus:
		ID = "SurfTorus"
		isNative = True
		class SurfTorus_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitiveCoil:
		ID = "PrimitiveCoil"
		isNative = True
		class PrimitiveCoil_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class Coil:
		ID = "Coil"
		isNative = True
		class Coil_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitiveCoil:
		ID = "SurfPrimitiveCoil"
		isNative = True
		class SurfPrimitiveCoil_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfCoil:
		ID = "SurfCoil"
		isNative = True
		class SurfCoil_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConnectorObstacleCmd:
		ID = "ConnectorObstacleCmd"
		isNative = True
		class ConnectorObstacleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConnectorObstacleEditCmd:
		ID = "ConnectorObstacleEditCmd"
		isNative = True
		class ConnectorObstacleEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PrimitivePipe:
		ID = "PrimitivePipe"
		isNative = True
		class PrimitivePipe_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PipePrimitiveEditCommand:
		ID = "PipePrimitiveEditCommand"
		isNative = True
		class PipePrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfPrimitivePipe:
		ID = "SurfPrimitivePipe"
		isNative = True
		class SurfPrimitivePipe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ThreeDprintCmdDef:
		ID = "ThreeDprintCmdDef"
		isNative = True
		class ThreeDprintCmdDef_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AutomatedModelingCommand:
		ID = "AutomatedModelingCommand"
		isNative = True
		class AutomatedModelingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionAutomatedModelingEditCommand:
		ID = "FusionAutomatedModelingEditCommand"
		isNative = True
		class FusionAutomatedModelingEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Box:
		ID = "Box"
		isNative = True
		class Box_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfBox:
		ID = "SurfBox"
		isNative = True
		class SurfBox_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Cylinder:
		ID = "Cylinder"
		isNative = True
		class Cylinder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfCylinder:
		ID = "SurfCylinder"
		isNative = True
		class SurfCylinder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Sphere:
		ID = "Sphere"
		isNative = True
		class Sphere_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfSphere:
		ID = "SurfSphere"
		isNative = True
		class SurfSphere_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfaceExtrude:
		ID = "SurfaceExtrude"
		isNative = True
		class SurfaceExtrude_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceExtrudeEditCommand:
		ID = "FusionSurfaceExtrudeEditCommand"
		isNative = True
		class FusionSurfaceExtrudeEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionExtendCommand:
		ID = "FusionExtendCommand"
		isNative = True
		class FusionExtendCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceExtendEditCommand:
		ID = "FusionDcSurfaceExtendEditCommand"
		isNative = True
		class FusionDcSurfaceExtendEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditFaceCommand:
		ID = "EditFaceCommand"
		isNative = True
		class EditFaceCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcFilletEditCommand:
		ID = "FusionDcFilletEditCommand"
		isNative = True
		class FusionDcFilletEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcFilletFeatureEditCommand:
		ID = "FusionDcFilletFeatureEditCommand"
		isNative = True
		class FusionDcFilletFeatureEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceThickenEditCommand:
		ID = "FusionDcSurfaceThickenEditCommand"
		isNative = True
		class FusionDcSurfaceThickenEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcChamferEditCommand:
		ID = "FusionDcChamferEditCommand"
		isNative = True
		class FusionDcChamferEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionComputeAllCommand:
		ID = "FusionComputeAllCommand"
		isNative = True
		class FusionComputeAllCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionComputeMinimumCommand:
		ID = "FusionComputeMinimumCommand"
		isNative = True
		class FusionComputeMinimumCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateXRefCommand:
		ID = "UpdateXRefCommand"
		isNative = True
		class UpdateXRefCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ChangeParameterCommand:
		ID = "ChangeParameterCommand"
		isNative = True
		class ChangeParameterCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionReorderCommand:
		ID = "FusionReorderCommand"
		isNative = True
		class FusionReorderCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConvertToDMFeatureCommand:
		ID = "ConvertToDMFeatureCommand"
		isNative = True
		class ConvertToDMFeatureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConvertToPMFeatureCommand:
		ID = "ConvertToPMFeatureCommand"
		isNative = True
		class ConvertToPMFeatureCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConvertToPMDesignCommand:
		ID = "ConvertToPMDesignCommand"
		isNative = True
		class ConvertToPMDesignCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConvertToDMDesignCommand:
		ID = "ConvertToDMDesignCommand"
		isNative = True
		class ConvertToDMDesignCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDumpGraphCommand:
		ID = "FusionDumpGraphCommand"
		isNative = True
		class FusionDumpGraphCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionLookupErrInfoCommand:
		ID = "FusionLookupErrInfoCommand"
		isNative = True
		class FusionLookupErrInfoCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SoftDeleteCommand:
		ID = "SoftDeleteCommand"
		isNative = True
		class SoftDeleteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BaseFeatureStop:
		ID = "BaseFeatureStop"
		isNative = True
		class BaseFeatureStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class BaseFeatureActivate:
		ID = "BaseFeatureActivate"
		isNative = True
		class BaseFeatureActivate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BaseFeatureCreationCommand:
		ID = "BaseFeatureCreationCommand"
		isNative = True
		class BaseFeatureCreationCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineBaseFeatureStop:
		ID = "TSplineBaseFeatureStop"
		isNative = True
		class TSplineBaseFeatureStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineBaseFeatureActivate:
		ID = "TSplineBaseFeatureActivate"
		isNative = True
		class TSplineBaseFeatureActivate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineBaseFeatureCreationCommand:
		ID = "TSplineBaseFeatureCreationCommand"
		isNative = True
		class TSplineBaseFeatureCreationCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshBaseFeatureStop:
		ID = "MeshBaseFeatureStop"
		isNative = True
		class MeshBaseFeatureStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeshBaseFeatureActivate:
		ID = "MeshBaseFeatureActivate"
		isNative = True
		class MeshBaseFeatureActivate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeshBaseFeatureCreationCommand:
		ID = "MeshBaseFeatureCreationCommand"
		isNative = True
		class MeshBaseFeatureCreationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRollCommand:
		ID = "FusionRollCommand"
		isNative = True
		class FusionRollCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionFindInTimeline:
		ID = "FusionFindInTimeline"
		isNative = True
		class FusionFindInTimeline_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionTrimFeaturesCommand:
		ID = "FusionTrimFeaturesCommand"
		isNative = True
		class FusionTrimFeaturesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionExpandGroupFeatureCommand:
		ID = "FusionExpandGroupFeatureCommand"
		isNative = True
		class FusionExpandGroupFeatureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateGroupFeatureCommand:
		ID = "FusionCreateGroupFeatureCommand"
		isNative = True
		class FusionCreateGroupFeatureCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionCollapseGroupFeatureCommand:
		ID = "FusionCollapseGroupFeatureCommand"
		isNative = True
		class FusionCollapseGroupFeatureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SnapshotCmd:
		ID = "SnapshotCmd"
		isNative = True
		class SnapshotCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SnapshotActivate:
		ID = "SnapshotActivate"
		isNative = True
		class SnapshotActivate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SnapshotEditAccept:
		ID = "SnapshotEditAccept"
		isNative = True
		class SnapshotEditAccept_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SnapshotEditCancel:
		ID = "SnapshotEditCancel"
		isNative = True
		class SnapshotEditCancel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AsBuiltPositionsCmd:
		ID = "AsBuiltPositionsCmd"
		isNative = True
		class AsBuiltPositionsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionOffsetFacesEditCommand:
		ID = "FusionOffsetFacesEditCommand"
		isNative = True
		class FusionOffsetFacesEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSuppressCommand:
		ID = "FusionSuppressCommand"
		isNative = True
		class FusionSuppressCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionUnsuppressCommand:
		ID = "FusionUnsuppressCommand"
		isNative = True
		class FusionUnsuppressCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class JointOrigin:
		ID = "JointOrigin"
		isNative = True
		class JointOrigin_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class JointAssembleCmdNew:
		ID = "JointAssembleCmdNew"
		isNative = True
		class JointAssembleCmdNew_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RigidGroupCmd:
		ID = "RigidGroupCmd"
		isNative = True
		class RigidGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditRigidGroupCmd:
		ID = "EditRigidGroupCmd"
		isNative = True
		class EditRigidGroupCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DcEditJointAssembleCmd:
		ID = "DcEditJointAssembleCmd"
		isNative = True
		class DcEditJointAssembleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DcEditRigidGroupCmd:
		ID = "DcEditRigidGroupCmd"
		isNative = True
		class DcEditRigidGroupCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditJointAssembleCmd:
		ID = "EditJointAssembleCmd"
		isNative = True
		class EditJointAssembleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditJointOriginCmd:
		ID = "EditJointOriginCmd"
		isNative = True
		class EditJointOriginCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditJointOriginR2Cmd:
		ID = "EditJointOriginR2Cmd"
		isNative = True
		class EditJointOriginR2Cmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class JointAsBuiltCmd:
		ID = "JointAsBuiltCmd"
		isNative = True
		class JointAsBuiltCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DcEditJointAsBuiltCmd:
		ID = "DcEditJointAsBuiltCmd"
		isNative = True
		class DcEditJointAsBuiltCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditJointDOFLimitsCmd:
		ID = "EditJointDOFLimitsCmd"
		isNative = True
		class EditJointDOFLimitsCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LockJointDOFCmd:
		ID = "LockJointDOFCmd"
		isNative = True
		class LockJointDOFCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnlockJointDOFCmd:
		ID = "UnlockJointDOFCmd"
		isNative = True
		class UnlockJointDOFCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMotionRelationshipCommand:
		ID = "FusionMotionRelationshipCommand"
		isNative = True
		class FusionMotionRelationshipCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditMotionRelationshipCmd:
		ID = "EditMotionRelationshipCmd"
		isNative = True
		class EditMotionRelationshipCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DcEditMotionRelationshipCmd:
		ID = "DcEditMotionRelationshipCmd"
		isNative = True
		class DcEditMotionRelationshipCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EnclosureCommand:
		ID = "EnclosureCommand"
		isNative = True
		class EnclosureCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DcEnclosureEditCommand:
		ID = "DcEnclosureEditCommand"
		isNative = True
		class DcEnclosureEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SelectByBoundaryCommand:
		ID = "SelectByBoundaryCommand"
		isNative = True
		class SelectByBoundaryCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MirrorCommand:
		ID = "MirrorCommand"
		isNative = True
		class MirrorCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PatternRectangular:
		ID = "PatternRectangular"
		isNative = True
		class PatternRectangular_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PatternRectangularEdit:
		ID = "PatternRectangularEdit"
		isNative = True
		class PatternRectangularEdit_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcRectangularPatternEditCommand:
		ID = "FusionDcRectangularPatternEditCommand"
		isNative = True
		class FusionDcRectangularPatternEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PatternOnPath:
		ID = "PatternOnPath"
		isNative = True
		class PatternOnPath_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PatternOnPathEdit:
		ID = "PatternOnPathEdit"
		isNative = True
		class PatternOnPathEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcPathPatternEditCommand:
		ID = "FusionDcPathPatternEditCommand"
		isNative = True
		class FusionDcPathPatternEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PatternCircular:
		ID = "PatternCircular"
		isNative = True
		class PatternCircular_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PatternCircularEdit:
		ID = "PatternCircularEdit"
		isNative = True
		class PatternCircularEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcCircularPatternEditCommand:
		ID = "FusionDcCircularPatternEditCommand"
		isNative = True
		class FusionDcCircularPatternEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcMirrorPatternEditCommand:
		ID = "FusionDcMirrorPatternEditCommand"
		isNative = True
		class FusionDcMirrorPatternEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcDraftEditCommand:
		ID = "FusionDcDraftEditCommand"
		isNative = True
		class FusionDcDraftEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ArrangeCommand:
		ID = "ArrangeCommand"
		isNative = True
		class ArrangeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DcArrangeEditCommand:
		ID = "DcArrangeEditCommand"
		isNative = True
		class DcArrangeEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DcArrangeEditSketchCommand:
		ID = "DcArrangeEditSketchCommand"
		isNative = True
		class DcArrangeEditSketchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionEditFeatureCommand:
		ID = "FusionEditFeatureCommand"
		isNative = True
		class FusionEditFeatureCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionEditDcFeatureCommand:
		ID = "FusionEditDcFeatureCommand"
		isNative = True
		class FusionEditDcFeatureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditDcFeatureProfileCommand:
		ID = "FusionEditDcFeatureProfileCommand"
		isNative = True
		class FusionEditDcFeatureProfileCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawSpline:
		ID = "DrawSpline"
		isNative = True
		class DrawSpline_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCVSpline:
		ID = "DrawCVSpline"
		isNative = True
		class DrawCVSpline_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCVMSpline3D:
		ID = "DrawCVMSpline3D"
		isNative = True
		class DrawCVMSpline3D_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCVMSpline5D:
		ID = "DrawCVMSpline5D"
		isNative = True
		class DrawCVMSpline5D_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCVSpline3D:
		ID = "DrawCVSpline3D"
		isNative = True
		class DrawCVSpline3D_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCVSpline5D:
		ID = "DrawCVSpline5D"
		isNative = True
		class DrawCVSpline5D_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionShowSketchPanelCmd:
		ID = "FusionShowSketchPanelCmd"
		isNative = True
		class FusionShowSketchPanelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class CircleCenterRadius:
		ID = "CircleCenterRadius"
		isNative = True
		class CircleCenterRadius_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CircleTwoPoint:
		ID = "CircleTwoPoint"
		isNative = True
		class CircleTwoPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CircleThreePoint:
		ID = "CircleThreePoint"
		isNative = True
		class CircleThreePoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CircleTanTanRadius:
		ID = "CircleTanTanRadius"
		isNative = True
		class CircleTanTanRadius_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CircleThreeTangent:
		ID = "CircleThreeTangent"
		isNative = True
		class CircleThreeTangent_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CircleElipse:
		ID = "CircleElipse"
		isNative = True
		class CircleElipse_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawRectangle:
		ID = "DrawRectangle"
		isNative = True
		class DrawRectangle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawCircle:
		ID = "DrawCircle"
		isNative = True
		class DrawCircle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawPolygon:
		ID = "DrawPolygon"
		isNative = True
		class DrawPolygon_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawArc:
		ID = "DrawArc"
		isNative = True
		class DrawArc_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawSlot:
		ID = "DrawSlot"
		isNative = True
		class DrawSlot_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeRectangleTwoPoint:
		ID = "ShapeRectangleTwoPoint"
		isNative = True
		class ShapeRectangleTwoPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeRectangleThreePoint:
		ID = "ShapeRectangleThreePoint"
		isNative = True
		class ShapeRectangleThreePoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeRectangleCenter:
		ID = "ShapeRectangleCenter"
		isNative = True
		class ShapeRectangleCenter_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ArcThreePoint:
		ID = "ArcThreePoint"
		isNative = True
		class ArcThreePoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ArcCenterTwoPoint:
		ID = "ArcCenterTwoPoint"
		isNative = True
		class ArcCenterTwoPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ArcTangent:
		ID = "ArcTangent"
		isNative = True
		class ArcTangent_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DrawPoint:
		ID = "DrawPoint"
		isNative = True
		class DrawPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapePolygonEdge:
		ID = "ShapePolygonEdge"
		isNative = True
		class ShapePolygonEdge_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapePolygonInscribed:
		ID = "ShapePolygonInscribed"
		isNative = True
		class ShapePolygonInscribed_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapePolygonCircumscribed:
		ID = "ShapePolygonCircumscribed"
		isNative = True
		class ShapePolygonCircumscribed_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConicCurveCmd:
		ID = "ConicCurveCmd"
		isNative = True
		class ConicCurveCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditConicCmd:
		ID = "EditConicCmd"
		isNative = True
		class EditConicCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShapeArcSlotThreePoint:
		ID = "ShapeArcSlotThreePoint"
		isNative = True
		class ShapeArcSlotThreePoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeArcSlotCenterTwoPoint:
		ID = "ShapeArcSlotCenterTwoPoint"
		isNative = True
		class ShapeArcSlotCenterTwoPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeSlotCenterToCenter:
		ID = "ShapeSlotCenterToCenter"
		isNative = True
		class ShapeSlotCenterToCenter_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeSlotOverall:
		ID = "ShapeSlotOverall"
		isNative = True
		class ShapeSlotOverall_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShapeSlotCenterPoint:
		ID = "ShapeSlotCenterPoint"
		isNative = True
		class ShapeSlotCenterPoint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FilletSketchCmd:
		ID = "FilletSketchCmd"
		isNative = True
		class FilletSketchCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ChamferSketchEqualDistance:
		ID = "ChamferSketchEqualDistance"
		isNative = True
		class ChamferSketchEqualDistance_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ChamferSketchDistanceDistance:
		ID = "ChamferSketchDistanceDistance"
		isNative = True
		class ChamferSketchDistanceDistance_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ChamferSketchDistanceAngle:
		ID = "ChamferSketchDistanceAngle"
		isNative = True
		class ChamferSketchDistanceAngle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchChamfer:
		ID = "SketchChamfer"
		isNative = True
		class SketchChamfer_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TrimSketchCmd:
		ID = "TrimSketchCmd"
		isNative = True
		class TrimSketchCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BreakSketchCmd:
		ID = "BreakSketchCmd"
		isNative = True
		class BreakSketchCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchScaleCmd:
		ID = "SketchScaleCmd"
		isNative = True
		class SketchScaleCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Offset:
		ID = "Offset"
		isNative = True
		class Offset_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionOffsetDragCommand:
		ID = "FusionOffsetDragCommand"
		isNative = True
		class FusionOffsetDragCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDragOffsetDimCommand:
		ID = "FusionDragOffsetDimCommand"
		isNative = True
		class FusionDragOffsetDimCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ExtendSketchCmd:
		ID = "ExtendSketchCmd"
		isNative = True
		class ExtendSketchCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class Project:
		ID = "Project"
		isNative = True
		class Project_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ProjectToSurface:
		ID = "ProjectToSurface"
		isNative = True
		class ProjectToSurface_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class Include3DGeometry:
		ID = "Include3DGeometry"
		isNative = True
		class Include3DGeometry_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MirrorSketchCommand:
		ID = "MirrorSketchCommand"
		isNative = True
		class MirrorSketchCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CircularSketchPatternCommand:
		ID = "CircularSketchPatternCommand"
		isNative = True
		class CircularSketchPatternCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchPatternCircularEdit:
		ID = "SketchPatternCircularEdit"
		isNative = True
		class SketchPatternCircularEdit_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OffsetSketchEdit:
		ID = "OffsetSketchEdit"
		isNative = True
		class OffsetSketchEdit_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RectangularSketchPatternCommand:
		ID = "RectangularSketchPatternCommand"
		isNative = True
		class RectangularSketchPatternCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchRectangularPatternEdit:
		ID = "SketchRectangularPatternEdit"
		isNative = True
		class SketchRectangularPatternEdit_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FitCurvesToSectionCommand:
		ID = "FitCurvesToSectionCommand"
		isNative = True
		class FitCurvesToSectionCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ProjectCutEdges:
		ID = "ProjectCutEdges"
		isNative = True
		class ProjectCutEdges_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IntersectionCurve:
		ID = "IntersectionCurve"
		isNative = True
		class IntersectionCurve_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ProjectSilhouette:
		ID = "ProjectSilhouette"
		isNative = True
		class ProjectSilhouette_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ProjectNewCmd:
		ID = "ProjectNewCmd"
		isNative = True
		class ProjectNewCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IntersectCmd:
		ID = "IntersectCmd"
		isNative = True
		class IntersectCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchDimension:
		ID = "SketchDimension"
		isNative = True
		class SketchDimension_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchEditDimensionCmdDef:
		ID = "SketchEditDimensionCmdDef"
		isNative = True
		class SketchEditDimensionCmdDef_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchDragDimension:
		ID = "SketchDragDimension"
		isNative = True
		class SketchDragDimension_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OffsetDimensionCmd:
		ID = "OffsetDimensionCmd"
		isNative = True
		class OffsetDimensionCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchGeomConstraintCmd:
		ID = "SketchGeomConstraintCmd"
		isNative = True
		class SketchGeomConstraintCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintCoincident:
		ID = "ConstraintCoincident"
		isNative = True
		class ConstraintCoincident_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintCollinear:
		ID = "ConstraintCollinear"
		isNative = True
		class ConstraintCollinear_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintConcentric:
		ID = "ConstraintConcentric"
		isNative = True
		class ConstraintConcentric_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintMidPoint:
		ID = "ConstraintMidPoint"
		isNative = True
		class ConstraintMidPoint_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintFix:
		ID = "ConstraintFix"
		isNative = True
		class ConstraintFix_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintParallel:
		ID = "ConstraintParallel"
		isNative = True
		class ConstraintParallel_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintPerpendicular:
		ID = "ConstraintPerpendicular"
		isNative = True
		class ConstraintPerpendicular_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintHorizontalVertical:
		ID = "ConstraintHorizontalVertical"
		isNative = True
		class ConstraintHorizontalVertical_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintTangent:
		ID = "ConstraintTangent"
		isNative = True
		class ConstraintTangent_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintEqual:
		ID = "ConstraintEqual"
		isNative = True
		class ConstraintEqual_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintSymmetry:
		ID = "ConstraintSymmetry"
		isNative = True
		class ConstraintSymmetry_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConstraintSmooth:
		ID = "ConstraintSmooth"
		isNative = True
		class ConstraintSmooth_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchFixConstraintCmd:
		ID = "SketchFixConstraintCmd"
		isNative = True
		class SketchFixConstraintCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchConstrainOnPlaneCmd:
		ID = "SketchConstrainOnPlaneCmd"
		isNative = True
		class SketchConstrainOnPlaneCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchImportSVG:
		ID = "SketchImportSVG"
		isNative = True
		class SketchImportSVG_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchExportToDXFCommand:
		ID = "SketchExportToDXFCommand"
		isNative = True
		class SketchExportToDXFCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchUnProjectCmd:
		ID = "SketchUnProjectCmd"
		isNative = True
		class SketchUnProjectCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteCoincidentConstraintCmd:
		ID = "DeleteCoincidentConstraintCmd"
		isNative = True
		class DeleteCoincidentConstraintCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDragSketchCommand:
		ID = "FusionDragSketchCommand"
		isNative = True
		class FusionDragSketchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SplineInsertPoint:
		ID = "SplineInsertPoint"
		isNative = True
		class SplineInsertPoint_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InsertControlPoint:
		ID = "InsertControlPoint"
		isNative = True
		class InsertControlPoint_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InsertControlPolygon:
		ID = "InsertControlPolygon"
		isNative = True
		class InsertControlPolygon_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SplineCloseCurve:
		ID = "SplineCloseCurve"
		isNative = True
		class SplineCloseCurve_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowProfile:
		ID = "ShowProfile"
		isNative = True
		class ShowProfile_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideProfile:
		ID = "HideProfile"
		isNative = True
		class HideProfile_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowDimension:
		ID = "ShowDimension"
		isNative = True
		class ShowDimension_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideDimension:
		ID = "HideDimension"
		isNative = True
		class HideDimension_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowDimensionWhenEditing:
		ID = "ShowDimensionWhenEditing"
		isNative = True
		class ShowDimensionWhenEditing_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideDimensionWhenEditing:
		ID = "HideDimensionWhenEditing"
		isNative = True
		class HideDimensionWhenEditing_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowConstraints:
		ID = "ShowConstraints"
		isNative = True
		class ShowConstraints_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideConstraints:
		ID = "HideConstraints"
		isNative = True
		class HideConstraints_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowSketchPoints:
		ID = "ShowSketchPoints"
		isNative = True
		class ShowSketchPoints_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideSketchPoints:
		ID = "HideSketchPoints"
		isNative = True
		class HideSketchPoints_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EnableFullyConstrained:
		ID = "EnableFullyConstrained"
		isNative = True
		class EnableFullyConstrained_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DisableFullyConstrained:
		ID = "DisableFullyConstrained"
		isNative = True
		class DisableFullyConstrained_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ToggleRadialDimCmd:
		ID = "ToggleRadialDimCmd"
		isNative = True
		class ToggleRadialDimCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ToggleDiameterDimCmd:
		ID = "ToggleDiameterDimCmd"
		isNative = True
		class ToggleDiameterDimCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ToggleDrivenDimCmd:
		ID = "ToggleDrivenDimCmd"
		isNative = True
		class ToggleDrivenDimCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ToggleDrivingDimCmd:
		ID = "ToggleDrivingDimCmd"
		isNative = True
		class ToggleDrivingDimCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowProjectedGeometries:
		ID = "ShowProjectedGeometries"
		isNative = True
		class ShowProjectedGeometries_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class HideProjectedGeometries:
		ID = "HideProjectedGeometries"
		isNative = True
		class HideProjectedGeometries_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchGridOn:
		ID = "SketchGridOn"
		isNative = True
		class SketchGridOn_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchGridOff:
		ID = "SketchGridOff"
		isNative = True
		class SketchGridOff_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchSnapOn:
		ID = "SketchSnapOn"
		isNative = True
		class SketchSnapOn_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchSnapOff:
		ID = "SketchSnapOff"
		isNative = True
		class SketchSnapOff_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SliceSketchCommand:
		ID = "SliceSketchCommand"
		isNative = True
		class SliceSketchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UnsliceSketchCommand:
		ID = "UnsliceSketchCommand"
		isNative = True
		class UnsliceSketchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowInactive:
		ID = "ShowInactive"
		isNative = True
		class ShowInactive_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TextCmd:
		ID = "TextCmd"
		isNative = True
		class TextCmd_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MTextCmd:
		ID = "MTextCmd"
		isNative = True
		class MTextCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AddTextGrip:
		ID = "AddTextGrip"
		isNative = True
		class AddTextGrip_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TextOnPathCmd:
		ID = "TextOnPathCmd"
		isNative = True
		class TextOnPathCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditTextCmd:
		ID = "EditTextCmd"
		isNative = True
		class EditTextCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditMTextCmd:
		ID = "EditMTextCmd"
		isNative = True
		class EditMTextCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExplodeTextCmd:
		ID = "ExplodeTextCmd"
		isNative = True
		class ExplodeTextCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchMoveTextCmd:
		ID = "SketchMoveTextCmd"
		isNative = True
		class SketchMoveTextCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AddTangentHandle:
		ID = "AddTangentHandle"
		isNative = True
		class AddTangentHandle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AddCurvatureHandle:
		ID = "AddCurvatureHandle"
		isNative = True
		class AddCurvatureHandle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DeleteTangentCommand:
		ID = "DeleteTangentCommand"
		isNative = True
		class DeleteTangentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DeleteCurvatureCommand:
		ID = "DeleteCurvatureCommand"
		isNative = True
		class DeleteCurvatureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchConstructionCmd:
		ID = "SketchConstructionCmd"
		isNative = True
		class SketchConstructionCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchToggleConstructionCmd:
		ID = "SketchToggleConstructionCmd"
		isNative = True
		class SketchToggleConstructionCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchCenterLineCmd:
		ID = "SketchCenterLineCmd"
		isNative = True
		class SketchCenterLineCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchToggleCenterLineCmd:
		ID = "SketchToggleCenterLineCmd"
		isNative = True
		class SketchToggleCenterLineCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchMoveCmd:
		ID = "SketchMoveCmd"
		isNative = True
		class SketchMoveCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SketchRedefineCommand:
		ID = "SketchRedefineCommand"
		isNative = True
		class SketchRedefineCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchRelinkProjectionCmd:
		ID = "SketchRelinkProjectionCmd"
		isNative = True
		class SketchRelinkProjectionCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionPressPullCommand:
		ID = "FusionPressPullCommand"
		isNative = True
		class FusionPressPullCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSelectBodiesBySizeCommand:
		ID = "FusionSelectBodiesBySizeCommand"
		isNative = True
		class FusionSelectBodiesBySizeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSelectSeedAndBoundaryFacesCommand:
		ID = "FusionSelectSeedAndBoundaryFacesCommand"
		isNative = True
		class FusionSelectSeedAndBoundaryFacesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionFindFeaturesCommand:
		ID = "FusionFindFeaturesCommand"
		isNative = True
		class FusionFindFeaturesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveFacesCommand:
		ID = "FusionRemoveFacesCommand"
		isNative = True
		class FusionRemoveFacesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveFacesEditCommand:
		ID = "FusionRemoveFacesEditCommand"
		isNative = True
		class FusionRemoveFacesEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveFeaturesCommand:
		ID = "FusionRemoveFeaturesCommand"
		isNative = True
		class FusionRemoveFeaturesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveFeaturesEditCommand:
		ID = "FusionRemoveFeaturesEditCommand"
		isNative = True
		class FusionRemoveFeaturesEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionRemoveDetailsCommand:
		ID = "FusionRemoveDetailsCommand"
		isNative = True
		class FusionRemoveDetailsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DissolveFeatureCmdDef:
		ID = "DissolveFeatureCmdDef"
		isNative = True
		class DissolveFeatureCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DissolveFeaturesCmdDef:
		ID = "DissolveFeaturesCmdDef"
		isNative = True
		class DissolveFeaturesCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DcReplaceWithPrimitiveEditCommand:
		ID = "DcReplaceWithPrimitiveEditCommand"
		isNative = True
		class DcReplaceWithPrimitiveEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReplaceWithPrimitivesCommand:
		ID = "ReplaceWithPrimitivesCommand"
		isNative = True
		class ReplaceWithPrimitivesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSpline2BRepCommand:
		ID = "TSpline2BRepCommand"
		isNative = True
		class TSpline2BRepCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConversionAnalysisCommand:
		ID = "ConversionAnalysisCommand"
		isNative = True
		class ConversionAnalysisCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneOffsetFromPlaneCommand:
		ID = "WorkPlaneOffsetFromPlaneCommand"
		isNative = True
		class WorkPlaneOffsetFromPlaneCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneByPlaneOffsetCommand:
		ID = "FusionDcEditWorkPlaneByPlaneOffsetCommand"
		isNative = True
		class FusionDcEditWorkPlaneByPlaneOffsetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneByLineAndAngleCommand:
		ID = "FusionDcEditWorkPlaneByLineAndAngleCommand"
		isNative = True
		class FusionDcEditWorkPlaneByLineAndAngleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneFromTwoPlanesCommand:
		ID = "FusionDcEditWorkPlaneFromTwoPlanesCommand"
		isNative = True
		class FusionDcEditWorkPlaneFromTwoPlanesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneFromTwoLinesCommand:
		ID = "FusionDcEditWorkPlaneFromTwoLinesCommand"
		isNative = True
		class FusionDcEditWorkPlaneFromTwoLinesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneTangentToCylinderCommand:
		ID = "FusionDcEditWorkPlaneTangentToCylinderCommand"
		isNative = True
		class FusionDcEditWorkPlaneTangentToCylinderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneTangentToFaceAtPointCommand:
		ID = "FusionDcEditWorkPlaneTangentToFaceAtPointCommand"
		isNative = True
		class FusionDcEditWorkPlaneTangentToFaceAtPointCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneFromThreePointsCommand:
		ID = "FusionDcEditWorkPlaneFromThreePointsCommand"
		isNative = True
		class FusionDcEditWorkPlaneFromThreePointsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPlaneAlongPathCommand:
		ID = "FusionDcEditWorkPlaneAlongPathCommand"
		isNative = True
		class FusionDcEditWorkPlaneAlongPathCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisThroughCylinderCommand:
		ID = "FusionDcEditWorkAxisThroughCylinderCommand"
		isNative = True
		class FusionDcEditWorkAxisThroughCylinderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisFromLineCommand:
		ID = "FusionDcEditWorkAxisFromLineCommand"
		isNative = True
		class FusionDcEditWorkAxisFromLineCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisFromTwoPointsCommand:
		ID = "FusionDcEditWorkAxisFromTwoPointsCommand"
		isNative = True
		class FusionDcEditWorkAxisFromTwoPointsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisFromTwoPlanesCommand:
		ID = "FusionDcEditWorkAxisFromTwoPlanesCommand"
		isNative = True
		class FusionDcEditWorkAxisFromTwoPlanesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisNormalToFaceCommand:
		ID = "FusionDcEditWorkAxisNormalToFaceCommand"
		isNative = True
		class FusionDcEditWorkAxisNormalToFaceCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkAxisFromPointAndFaceCommand:
		ID = "FusionDcEditWorkAxisFromPointAndFaceCommand"
		isNative = True
		class FusionDcEditWorkAxisFromPointAndFaceCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointCommand:
		ID = "FusionDcEditWorkPointCommand"
		isNative = True
		class FusionDcEditWorkPointCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointFromTwoLinesCommand:
		ID = "FusionDcEditWorkPointFromTwoLinesCommand"
		isNative = True
		class FusionDcEditWorkPointFromTwoLinesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointFromThreePlanesCommand:
		ID = "FusionDcEditWorkPointFromThreePlanesCommand"
		isNative = True
		class FusionDcEditWorkPointFromThreePlanesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointFromCircleOrSphereCommand:
		ID = "FusionDcEditWorkPointFromCircleOrSphereCommand"
		isNative = True
		class FusionDcEditWorkPointFromCircleOrSphereCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointFromLineAndPlaneCommand:
		ID = "FusionDcEditWorkPointFromLineAndPlaneCommand"
		isNative = True
		class FusionDcEditWorkPointFromLineAndPlaneCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditWorkPointAlongPathCommand:
		ID = "FusionDcEditWorkPointAlongPathCommand"
		isNative = True
		class FusionDcEditWorkPointAlongPathCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromLineAndAngleCommand:
		ID = "WorkPlaneFromLineAndAngleCommand"
		isNative = True
		class WorkPlaneFromLineAndAngleCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneTangentToCylinderCommand:
		ID = "WorkPlaneTangentToCylinderCommand"
		isNative = True
		class WorkPlaneTangentToCylinderCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromTwoPlanesCommand:
		ID = "WorkPlaneFromTwoPlanesCommand"
		isNative = True
		class WorkPlaneFromTwoPlanesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromTwoLinesCommand:
		ID = "WorkPlaneFromTwoLinesCommand"
		isNative = True
		class WorkPlaneFromTwoLinesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromThreePointsCommand:
		ID = "WorkPlaneFromThreePointsCommand"
		isNative = True
		class WorkPlaneFromThreePointsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisThroughCylinderCommand:
		ID = "WorkAxisThroughCylinderCommand"
		isNative = True
		class WorkAxisThroughCylinderCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisFromTwoPlanesCommand:
		ID = "WorkAxisFromTwoPlanesCommand"
		isNative = True
		class WorkAxisFromTwoPlanesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisFromTwoPointsCommand:
		ID = "WorkAxisFromTwoPointsCommand"
		isNative = True
		class WorkAxisFromTwoPointsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisNormalToFaceCommand:
		ID = "WorkAxisNormalToFaceCommand"
		isNative = True
		class WorkAxisNormalToFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromThreePlanesCommand:
		ID = "WorkPointFromThreePlanesCommand"
		isNative = True
		class WorkPointFromThreePlanesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromTwoLinesCommand:
		ID = "WorkPointFromTwoLinesCommand"
		isNative = True
		class WorkPointFromTwoLinesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromPointCommand:
		ID = "WorkPointFromPointCommand"
		isNative = True
		class WorkPointFromPointCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromCircleOrSphereCommand:
		ID = "WorkPointFromCircleOrSphereCommand"
		isNative = True
		class WorkPointFromCircleOrSphereCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromLineAndPlaneCommand:
		ID = "WorkPointFromLineAndPlaneCommand"
		isNative = True
		class WorkPointFromLineAndPlaneCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointAlongPathCommand:
		ID = "WorkPointAlongPathCommand"
		isNative = True
		class WorkPointAlongPathCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPointFromCoordsCommand:
		ID = "WorkPointFromCoordsCommand"
		isNative = True
		class WorkPointFromCoordsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisFromLineCommand:
		ID = "WorkAxisFromLineCommand"
		isNative = True
		class WorkAxisFromLineCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkAxisFromPointAndFaceCommand:
		ID = "WorkAxisFromPointAndFaceCommand"
		isNative = True
		class WorkAxisFromPointAndFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromPointAndFaceCommand:
		ID = "WorkPlaneFromPointAndFaceCommand"
		isNative = True
		class WorkPlaneFromPointAndFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneFromPointAndNormalCommand:
		ID = "WorkPlaneFromPointAndNormalCommand"
		isNative = True
		class WorkPlaneFromPointAndNormalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WorkPlaneAlongPathCommand:
		ID = "WorkPlaneAlongPathCommand"
		isNative = True
		class WorkPlaneAlongPathCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDragWorkAxisExtentCommand:
		ID = "FusionDragWorkAxisExtentCommand"
		isNative = True
		class FusionDragWorkAxisExtentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDragWorkPlaneExtentCommand:
		ID = "FusionDragWorkPlaneExtentCommand"
		isNative = True
		class FusionDragWorkPlaneExtentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateNewComponentCommand:
		ID = "FusionCreateNewComponentCommand"
		isNative = True
		class FusionCreateNewComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateNewCompCmdFromBody:
		ID = "FusionCreateNewCompCmdFromBody"
		isNative = True
		class FusionCreateNewCompCmdFromBody_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateNewCompCmdFromSel:
		ID = "FusionCreateNewCompCmdFromSel"
		isNative = True
		class FusionCreateNewCompCmdFromSel_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateComponentFromBodyEditCommand:
		ID = "FusionCreateComponentFromBodyEditCommand"
		isNative = True
		class FusionCreateComponentFromBodyEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionExportComponentCommand:
		ID = "FusionExportComponentCommand"
		isNative = True
		class FusionExportComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSaveAsComponentCommand:
		ID = "FusionSaveAsComponentCommand"
		isNative = True
		class FusionSaveAsComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSaveAsAndReplaceComponentCommand:
		ID = "FusionSaveAsAndReplaceComponentCommand"
		isNative = True
		class FusionSaveAsAndReplaceComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSaveAsSTLCommand:
		ID = "FusionSaveAsSTLCommand"
		isNative = True
		class FusionSaveAsSTLCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GrabCadExportSTLCommand:
		ID = "GrabCadExportSTLCommand"
		isNative = True
		class GrabCadExportSTLCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSaveAsOBJCommand:
		ID = "FusionSaveAsOBJCommand"
		isNative = True
		class FusionSaveAsOBJCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSaveControlFrameAsOBJCommand:
		ID = "FusionSaveControlFrameAsOBJCommand"
		isNative = True
		class FusionSaveControlFrameAsOBJCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineSaveAsIGACommand:
		ID = "TSplineSaveAsIGACommand"
		isNative = True
		class TSplineSaveAsIGACommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionActivateLocalCompCmd:
		ID = "FusionActivateLocalCompCmd"
		isNative = True
		class FusionActivateLocalCompCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BeginEditInPlaceCmd:
		ID = "BeginEditInPlaceCmd"
		isNative = True
		class BeginEditInPlaceCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BeginEIPAsEditContextCmd:
		ID = "BeginEIPAsEditContextCmd"
		isNative = True
		class BeginEIPAsEditContextCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BeginEIPAsActivateContextCmd:
		ID = "BeginEIPAsActivateContextCmd"
		isNative = True
		class BeginEIPAsActivateContextCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ContextUpdateFromParentCmd:
		ID = "ContextUpdateFromParentCmd"
		isNative = True
		class ContextUpdateFromParentCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ContextUpdateAllFromParentCmd:
		ID = "ContextUpdateAllFromParentCmd"
		isNative = True
		class ContextUpdateAllFromParentCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EndEditInPlaceCmd:
		ID = "EndEditInPlaceCmd"
		isNative = True
		class EndEditInPlaceCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EndEIPAsEditContextCmd:
		ID = "EndEIPAsEditContextCmd"
		isNative = True
		class EndEIPAsEditContextCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EndEIPAsActivateContextCmd:
		ID = "EndEIPAsActivateContextCmd"
		isNative = True
		class EndEIPAsActivateContextCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPContextActivateCmd:
		ID = "EIPContextActivateCmd"
		isNative = True
		class EIPContextActivateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPContextActivateAsEditCmd:
		ID = "EIPContextActivateAsEditCmd"
		isNative = True
		class EIPContextActivateAsEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EIPLocalContextActivateCmdDef:
		ID = "EIPLocalContextActivateCmdDef"
		isNative = True
		class EIPLocalContextActivateCmdDef_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPContextUpdateCmd:
		ID = "EIPContextUpdateCmd"
		isNative = True
		class EIPContextUpdateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPContextBreakLinkCmd:
		ID = "EIPContextBreakLinkCmd"
		isNative = True
		class EIPContextBreakLinkCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPNonAssociativeToggleCmd:
		ID = "EIPNonAssociativeToggleCmd"
		isNative = True
		class EIPNonAssociativeToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EIPAssociativeToggleCmd:
		ID = "EIPAssociativeToggleCmd"
		isNative = True
		class EIPAssociativeToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ReferenceObjectsCmd:
		ID = "ReferenceObjectsCmd"
		isNative = True
		class ReferenceObjectsCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionCreateSurfaceGroupCommand:
		ID = "FusionCreateSurfaceGroupCommand"
		isNative = True
		class FusionCreateSurfaceGroupCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionMoveToSurfaceGroupCommand:
		ID = "FusionMoveToSurfaceGroupCommand"
		isNative = True
		class FusionMoveToSurfaceGroupCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionPasteNewCommand:
		ID = "FusionPasteNewCommand"
		isNative = True
		class FusionPasteNewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMakeIndependentCommand:
		ID = "FusionMakeIndependentCommand"
		isNative = True
		class FusionMakeIndependentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionPropertiesCommand:
		ID = "FusionPropertiesCommand"
		isNative = True
		class FusionPropertiesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityControlCmd:
		ID = "OpacityControlCmd"
		isNative = True
		class OpacityControlCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CustomOpacityControlCmd:
		ID = "CustomOpacityControlCmd"
		isNative = True
		class CustomOpacityControlCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlTenCmd:
		ID = "OpacityCtrlTenCmd"
		isNative = True
		class OpacityCtrlTenCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlTwentyCmd:
		ID = "OpacityCtrlTwentyCmd"
		isNative = True
		class OpacityCtrlTwentyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlThirtyCmd:
		ID = "OpacityCtrlThirtyCmd"
		isNative = True
		class OpacityCtrlThirtyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlFortyCmd:
		ID = "OpacityCtrlFortyCmd"
		isNative = True
		class OpacityCtrlFortyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlFiftyCmd:
		ID = "OpacityCtrlFiftyCmd"
		isNative = True
		class OpacityCtrlFiftyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlSixtyCmd:
		ID = "OpacityCtrlSixtyCmd"
		isNative = True
		class OpacityCtrlSixtyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlSeventyCmd:
		ID = "OpacityCtrlSeventyCmd"
		isNative = True
		class OpacityCtrlSeventyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlEightyCmd:
		ID = "OpacityCtrlEightyCmd"
		isNative = True
		class OpacityCtrlEightyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlNinetyCmd:
		ID = "OpacityCtrlNinetyCmd"
		isNative = True
		class OpacityCtrlNinetyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpacityCtrlHundredCmd:
		ID = "OpacityCtrlHundredCmd"
		isNative = True
		class OpacityCtrlHundredCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TessellationControlCmd:
		ID = "TessellationControlCmd"
		isNative = True
		class TessellationControlCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DielectricPriorityControlCmd:
		ID = "DielectricPriorityControlCmd"
		isNative = True
		class DielectricPriorityControlCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionAddBackgroundCanvasCommand:
		ID = "FusionAddBackgroundCanvasCommand"
		isNative = True
		class FusionAddBackgroundCanvasCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionAddCanvasCommand:
		ID = "FusionAddCanvasCommand"
		isNative = True
		class FusionAddCanvasCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditCanvasCommand:
		ID = "FusionDcEditCanvasCommand"
		isNative = True
		class FusionDcEditCanvasCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionEditCanvasCommand:
		ID = "FusionEditCanvasCommand"
		isNative = True
		class FusionEditCanvasCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCalibrateCanvasCommand:
		ID = "FusionCalibrateCanvasCommand"
		isNative = True
		class FusionCalibrateCanvasCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionAddDecalCommand:
		ID = "FusionAddDecalCommand"
		isNative = True
		class FusionAddDecalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionAddEditDecalCommand:
		ID = "FusionAddEditDecalCommand"
		isNative = True
		class FusionAddEditDecalCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcEditDecalCommand:
		ID = "FusionDcEditDecalCommand"
		isNative = True
		class FusionDcEditDecalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionEditDecalCommand:
		ID = "FusionEditDecalCommand"
		isNative = True
		class FusionEditDecalCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionReplaceDecalImageCommand:
		ID = "FusionReplaceDecalImageCommand"
		isNative = True
		class FusionReplaceDecalImageCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionReplaceCanvasImageCommand:
		ID = "FusionReplaceCanvasImageCommand"
		isNative = True
		class FusionReplaceCanvasImageCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionViewColorCyclingToggleCmd:
		ID = "FusionViewColorCyclingToggleCmd"
		isNative = True
		class FusionViewColorCyclingToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AnalysisVisibilityToggleCmd:
		ID = "AnalysisVisibilityToggleCmd"
		isNative = True
		class AnalysisVisibilityToggleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCurvatureCombAnalysisCommand:
		ID = "FusionCurvatureCombAnalysisCommand"
		isNative = True
		class FusionCurvatureCombAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditCurvatureCombAnalysisCommand:
		ID = "FusionEditCurvatureCombAnalysisCommand"
		isNative = True
		class FusionEditCurvatureCombAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionToggleSetupCurveCurvatureCombCommand:
		ID = "FusionToggleSetupCurveCurvatureCombCommand"
		isNative = True
		class FusionToggleSetupCurveCurvatureCombCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionToggleCurveCurvatureCombCommand:
		ID = "FusionToggleCurveCurvatureCombCommand"
		isNative = True
		class FusionToggleCurveCurvatureCombCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCurveCurvatureCombSetupCommand:
		ID = "FusionCurveCurvatureCombSetupCommand"
		isNative = True
		class FusionCurveCurvatureCombSetupCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionZebraAnalysisCommand:
		ID = "FusionZebraAnalysisCommand"
		isNative = True
		class FusionZebraAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditZebraAnalysisCommand:
		ID = "FusionEditZebraAnalysisCommand"
		isNative = True
		class FusionEditZebraAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDraftAnalysisCommand:
		ID = "FusionDraftAnalysisCommand"
		isNative = True
		class FusionDraftAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditDraftAnalysisCommand:
		ID = "FusionEditDraftAnalysisCommand"
		isNative = True
		class FusionEditDraftAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCurvatureMapAnalysisCommand:
		ID = "FusionCurvatureMapAnalysisCommand"
		isNative = True
		class FusionCurvatureMapAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditCurvatureMapAnalysisCommand:
		ID = "FusionEditCurvatureMapAnalysisCommand"
		isNative = True
		class FusionEditCurvatureMapAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionAccessibilityAnalysisCommand:
		ID = "FusionAccessibilityAnalysisCommand"
		isNative = True
		class FusionAccessibilityAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditAccessibilityAnalysisCommand:
		ID = "FusionEditAccessibilityAnalysisCommand"
		isNative = True
		class FusionEditAccessibilityAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionMinimumRadiusAnalysisCommand:
		ID = "FusionMinimumRadiusAnalysisCommand"
		isNative = True
		class FusionMinimumRadiusAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditMinimumRadiusAnalysisCommand:
		ID = "FusionEditMinimumRadiusAnalysisCommand"
		isNative = True
		class FusionEditMinimumRadiusAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionIsoCurveAnalysisCommand:
		ID = "FusionIsoCurveAnalysisCommand"
		isNative = True
		class FusionIsoCurveAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditIsoCurveAnalysisCommand:
		ID = "FusionEditIsoCurveAnalysisCommand"
		isNative = True
		class FusionEditIsoCurveAnalysisCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionHalfSectionViewCommand:
		ID = "FusionHalfSectionViewCommand"
		isNative = True
		class FusionHalfSectionViewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditHalfSectionViewCommand:
		ID = "FusionEditHalfSectionViewCommand"
		isNative = True
		class FusionEditHalfSectionViewCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionCenterOfMassCommand:
		ID = "FusionCenterOfMassCommand"
		isNative = True
		class FusionCenterOfMassCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionEditCenterOfMassCommand:
		ID = "FusionEditCenterOfMassCommand"
		isNative = True
		class FusionEditCenterOfMassCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GrabCadSaveDocumentCommand:
		ID = "GrabCadSaveDocumentCommand"
		isNative = True
		class GrabCadSaveDocumentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GrabCadSaveDocumentAsCommand:
		ID = "GrabCadSaveDocumentAsCommand"
		isNative = True
		class GrabCadSaveDocumentAsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GrabCadExportCommand:
		ID = "GrabCadExportCommand"
		isNative = True
		class GrabCadExportCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GrabCadViewProjectCommand:
		ID = "GrabCadViewProjectCommand"
		isNative = True
		class GrabCadViewProjectCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionPublishToGrabCADCommand:
		ID = "FusionPublishToGrabCADCommand"
		isNative = True
		class FusionPublishToGrabCADCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShareToFusion360GalleryCommand:
		ID = "ShareToFusion360GalleryCommand"
		isNative = True
		class ShareToFusion360GalleryCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShareToFusion360GallerySubCommand:
		ID = "ShareToFusion360GallerySubCommand"
		isNative = True
		class ShareToFusion360GallerySubCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenGrabFileCommand:
		ID = "OpenGrabFileCommand"
		isNative = True
		class OpenGrabFileCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenHubFileCommand:
		ID = "OpenHubFileCommand"
		isNative = True
		class OpenHubFileCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenNonFusionCADFileCommand:
		ID = "OpenNonFusionCADFileCommand"
		isNative = True
		class OpenNonFusionCADFileCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenAddInSupportedFileCommand:
		ID = "OpenAddInSupportedFileCommand"
		isNative = True
		class OpenAddInSupportedFileCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AddInSupportedFileCommand:
		ID = "AddInSupportedFileCommand"
		isNative = True
		class AddInSupportedFileCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class selectWindow:
		ID = "selectWindow"
		isNative = True
		class selectWindow_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class selectFreeForm:
		ID = "selectFreeForm"
		isNative = True
		class selectFreeForm_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class selectPaint:
		ID = "selectPaint"
		isNative = True
		class selectPaint_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class selectAdjacent:
		ID = "selectAdjacent"
		isNative = True
		class selectAdjacent_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionRenameTimelineEntryCommand:
		ID = "FusionRenameTimelineEntryCommand"
		isNative = True
		class FusionRenameTimelineEntryCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BreakXRefLinkCmd:
		ID = "BreakXRefLinkCmd"
		isNative = True
		class BreakXRefLinkCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ChooseVersionCmd:
		ID = "ChooseVersionCmd"
		isNative = True
		class ChooseVersionCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowHistoryCmd:
		ID = "ShowHistoryCmd"
		isNative = True
		class ShowHistoryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360RefreshDocumentCommand:
		ID = "PLM360RefreshDocumentCommand"
		isNative = True
		class PLM360RefreshDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360DeepRefreshDocumentCommand:
		ID = "PLM360DeepRefreshDocumentCommand"
		isNative = True
		class PLM360DeepRefreshDocumentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GetLatestCmd:
		ID = "GetLatestCmd"
		isNative = True
		class GetLatestCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GetLatestMilestoneCmd:
		ID = "GetLatestMilestoneCmd"
		isNative = True
		class GetLatestMilestoneCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class GetAllLatestCmd:
		ID = "GetAllLatestCmd"
		isNative = True
		class GetAllLatestCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateAllLatestCmd:
		ID = "UpdateAllLatestCmd"
		isNative = True
		class UpdateAllLatestCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectByInvertCommand:
		ID = "SelectByInvertCommand"
		isNative = True
		class SelectByInvertCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSelectAllOccurrencesCommand:
		ID = "FusionSelectAllOccurrencesCommand"
		isNative = True
		class FusionSelectAllOccurrencesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSelectSimilarOccurrencesCommand:
		ID = "FusionSelectSimilarOccurrencesCommand"
		isNative = True
		class FusionSelectSimilarOccurrencesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InsertMcMasterCarrComponentCommand:
		ID = "InsertMcMasterCarrComponentCommand"
		isNative = True
		class InsertMcMasterCarrComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ImportDxfFileCommand:
		ID = "ImportDxfFileCommand"
		isNative = True
		class ImportDxfFileCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SelectByNameCommand:
		ID = "SelectByNameCommand"
		isNative = True
		class SelectByNameCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ActivateWorkingModelAssetCommand:
		ID = "ActivateWorkingModelAssetCommand"
		isNative = True
		class ActivateWorkingModelAssetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CreateWorkingModelAssetCommand:
		ID = "CreateWorkingModelAssetCommand"
		isNative = True
		class CreateWorkingModelAssetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateAssociativeCloneCommand:
		ID = "UpdateAssociativeCloneCommand"
		isNative = True
		class UpdateAssociativeCloneCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateLightweightWorkingModel:
		ID = "UpdateLightweightWorkingModel"
		isNative = True
		class UpdateLightweightWorkingModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class BreakWorkingModelLinkCmd:
		ID = "BreakWorkingModelLinkCmd"
		isNative = True
		class BreakWorkingModelLinkCmd_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PullDeriveCommand:
		ID = "PullDeriveCommand"
		isNative = True
		class PullDeriveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenDeriveDocumentCommand:
		ID = "OpenDeriveDocumentCommand"
		isNative = True
		class OpenDeriveDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360SaveAsLatestCommand:
		ID = "PLM360SaveAsLatestCommand"
		isNative = True
		class PLM360SaveAsLatestCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PLM360SaveAsLatestOnQATCommand:
		ID = "PLM360SaveAsLatestOnQATCommand"
		isNative = True
		class PLM360SaveAsLatestOnQATCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditDeriveCommand:
		ID = "EditDeriveCommand"
		isNative = True
		class EditDeriveCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PushDeriveCommand:
		ID = "PushDeriveCommand"
		isNative = True
		class PushDeriveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class EditDeriveSourceCommand:
		ID = "EditDeriveSourceCommand"
		isNative = True
		class EditDeriveSourceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class BreakExternalDeriveLinkCmd:
		ID = "BreakExternalDeriveLinkCmd"
		isNative = True
		class BreakExternalDeriveLinkCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenCommand:
		ID = "OpenCommand"
		isNative = True
		class OpenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ShowInsertDialogCommand:
		ID = "ShowInsertDialogCommand"
		isNative = True
		class ShowInsertDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchAutoConstrainCmd:
		ID = "SketchAutoConstrainCmd"
		isNative = True
		class SketchAutoConstrainCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideInsertDialogCommand:
		ID = "HideInsertDialogCommand"
		isNative = True
		class HideInsertDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InsertDialogCommand:
		ID = "InsertDialogCommand"
		isNative = True
		class InsertDialogCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class APIFeatureEditCommand:
		ID = "APIFeatureEditCommand"
		isNative = True
		class APIFeatureEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InstallAppAddInCommand:
		ID = "InstallAppAddInCommand"
		isNative = True
		class InstallAppAddInCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineImportCommand:
		ID = "TSplineImportCommand"
		isNative = True
		class TSplineImportCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineEditCommand:
		ID = "TSplineEditCommand"
		isNative = True
		class TSplineEditCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineExtrudeCommand:
		ID = "TSplineExtrudeCommand"
		isNative = True
		class TSplineExtrudeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineRevolveCommand:
		ID = "TSplineRevolveCommand"
		isNative = True
		class TSplineRevolveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineSweepCommand:
		ID = "TSplineSweepCommand"
		isNative = True
		class TSplineSweepCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineInsertEdgeCommand:
		ID = "TSplineInsertEdgeCommand"
		isNative = True
		class TSplineInsertEdgeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineSlideEdgeCommand:
		ID = "TSplineSlideEdgeCommand"
		isNative = True
		class TSplineSlideEdgeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineBevelEdgeCommand:
		ID = "TSplineBevelEdgeCommand"
		isNative = True
		class TSplineBevelEdgeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineInsertPointCommand:
		ID = "TSplineInsertPointCommand"
		isNative = True
		class TSplineInsertPointCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineThickenCommand:
		ID = "TSplineThickenCommand"
		isNative = True
		class TSplineThickenCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineWeldCommand:
		ID = "TSplineWeldCommand"
		isNative = True
		class TSplineWeldCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineUnWeldCommand:
		ID = "TSplineUnWeldCommand"
		isNative = True
		class TSplineUnWeldCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitivePlaneCommand:
		ID = "TSplinePrimitivePlaneCommand"
		isNative = True
		class TSplinePrimitivePlaneCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitiveBoxCommand:
		ID = "TSplinePrimitiveBoxCommand"
		isNative = True
		class TSplinePrimitiveBoxCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitiveCylinderCommand:
		ID = "TSplinePrimitiveCylinderCommand"
		isNative = True
		class TSplinePrimitiveCylinderCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitiveSphereCommand:
		ID = "TSplinePrimitiveSphereCommand"
		isNative = True
		class TSplinePrimitiveSphereCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitiveQuadBallCommand:
		ID = "TSplinePrimitiveQuadBallCommand"
		isNative = True
		class TSplinePrimitiveQuadBallCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitiveTorusCommand:
		ID = "TSplinePrimitiveTorusCommand"
		isNative = True
		class TSplinePrimitiveTorusCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineInternalMirrorSymmetryCmd:
		ID = "TSplineInternalMirrorSymmetryCmd"
		isNative = True
		class TSplineInternalMirrorSymmetryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineInternalCircularSymmetryCmd:
		ID = "TSplineInternalCircularSymmetryCmd"
		isNative = True
		class TSplineInternalCircularSymmetryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineReflectionMirrorSymmetryCmd:
		ID = "TSplineReflectionMirrorSymmetryCmd"
		isNative = True
		class TSplineReflectionMirrorSymmetryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineReflectionCircularSymmetryCmd:
		ID = "TSplineReflectionCircularSymmetryCmd"
		isNative = True
		class TSplineReflectionCircularSymmetryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineClearSymmetryCommand:
		ID = "TSplineClearSymmetryCommand"
		isNative = True
		class TSplineClearSymmetryCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineAppendFaceCommand:
		ID = "TSplineAppendFaceCommand"
		isNative = True
		class TSplineAppendFaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineToggleTessModeCmd:
		ID = "TSplineToggleTessModeCmd"
		isNative = True
		class TSplineToggleTessModeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineCapSettingCommand:
		ID = "TSplineCapSettingCommand"
		isNative = True
		class TSplineCapSettingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineFillHoleCmd:
		ID = "TSplineFillHoleCmd"
		isNative = True
		class TSplineFillHoleCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineEraseAndFillCmd:
		ID = "TSplineEraseAndFillCmd"
		isNative = True
		class TSplineEraseAndFillCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineSubsetCmd:
		ID = "TSplineSubsetCmd"
		isNative = True
		class TSplineSubsetCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineSmoothCmd:
		ID = "TSplineSmoothCmd"
		isNative = True
		class TSplineSmoothCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineCylindrifyCmd:
		ID = "TSplineCylindrifyCmd"
		isNative = True
		class TSplineCylindrifyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineMakeUniformCmd:
		ID = "TSplineMakeUniformCmd"
		isNative = True
		class TSplineMakeUniformCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineCreasedEdgeCommand:
		ID = "TSplineCreasedEdgeCommand"
		isNative = True
		class TSplineCreasedEdgeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineUnCreaseEdgeCmd:
		ID = "TSplineUnCreaseEdgeCmd"
		isNative = True
		class TSplineUnCreaseEdgeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineBridgeSubDCmd:
		ID = "TSplineBridgeSubDCmd"
		isNative = True
		class TSplineBridgeSubDCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineMergeEdgeCmd:
		ID = "TSplineMergeEdgeCmd"
		isNative = True
		class TSplineMergeEdgeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineFlattenSubDCmd:
		ID = "TSplineFlattenSubDCmd"
		isNative = True
		class TSplineFlattenSubDCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineStraightenCmd:
		ID = "TSplineStraightenCmd"
		isNative = True
		class TSplineStraightenCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineEditByCurveCmd:
		ID = "TSplineEditByCurveCmd"
		isNative = True
		class TSplineEditByCurveCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePullSubDCmd:
		ID = "TSplinePullSubDCmd"
		isNative = True
		class TSplinePullSubDCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineInterpolateSubDCmd:
		ID = "TSplineInterpolateSubDCmd"
		isNative = True
		class TSplineInterpolateSubDCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineRepairBodyCmd:
		ID = "TSplineRepairBodyCmd"
		isNative = True
		class TSplineRepairBodyCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineMatchCmd:
		ID = "TSplineMatchCmd"
		isNative = True
		class TSplineMatchCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePrimitivePipe:
		ID = "TSplinePrimitivePipe"
		isNative = True
		class TSplinePrimitivePipe_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplinePipeEditCommand:
		ID = "TSplinePipeEditCommand"
		isNative = True
		class TSplinePipeEditCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineIsolateSymmetryCmd:
		ID = "TSplineIsolateSymmetryCmd"
		isNative = True
		class TSplineIsolateSymmetryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineDumpEntityCommand:
		ID = "TSplineDumpEntityCommand"
		isNative = True
		class TSplineDumpEntityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineSaveAsTSMCommand:
		ID = "TSplineSaveAsTSMCommand"
		isNative = True
		class TSplineSaveAsTSMCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineDiagnosticCommand:
		ID = "TSplineDiagnosticCommand"
		isNative = True
		class TSplineDiagnosticCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AssemblyInfoCommand:
		ID = "AssemblyInfoCommand"
		isNative = True
		class AssemblyInfoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TSplineFreezeCmd:
		ID = "TSplineFreezeCmd"
		isNative = True
		class TSplineFreezeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class TSplineUnFreezeCmd:
		ID = "TSplineUnFreezeCmd"
		isNative = True
		class TSplineUnFreezeCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ActivateWorkingModelCommand:
		ID = "ActivateWorkingModelCommand"
		isNative = True
		class ActivateWorkingModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActivateGenWorkingModelCommand:
		ID = "ActivateGenWorkingModelCommand"
		isNative = True
		class ActivateGenWorkingModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CopyWorkingModelCommand:
		ID = "CopyWorkingModelCommand"
		isNative = True
		class CopyWorkingModelCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteWorkingModelCommand:
		ID = "DeleteWorkingModelCommand"
		isNative = True
		class DeleteWorkingModelCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CopyWorkingModelAndImportCommand:
		ID = "CopyWorkingModelAndImportCommand"
		isNative = True
		class CopyWorkingModelAndImportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ExtractTSSurfaceBodyCommand:
		ID = "ExtractTSSurfaceBodyCommand"
		isNative = True
		class ExtractTSSurfaceBodyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ConvertSurfaceBody2TSCommand:
		ID = "ConvertSurfaceBody2TSCommand"
		isNative = True
		class ConvertSurfaceBody2TSCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FinishSimplifyCommand:
		ID = "FinishSimplifyCommand"
		isNative = True
		class FinishSimplifyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishEditModelCommand:
		ID = "FinishEditModelCommand"
		isNative = True
		class FinishEditModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDeleteOverrideCommand:
		ID = "FusionDeleteOverrideCommand"
		isNative = True
		class FusionDeleteOverrideCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SoftDeleteAllUnselectedCommand:
		ID = "SoftDeleteAllUnselectedCommand"
		isNative = True
		class SoftDeleteAllUnselectedCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewPLMOfflineFusionDrawingItemBasedFusionCommand:
		ID = "NewPLMOfflineFusionDrawingItemBasedFusionCommand"
		isNative = True
		class NewPLMOfflineFusionDrawingItemBasedFusionCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewDrawingMenuCommand:
		ID = "NewDrawingMenuCommand"
		isNative = True
		class NewDrawingMenuCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCreateFromComponentsCommand:
		ID = "FusionDrawingCreateFromComponentsCommand"
		isNative = True
		class FusionDrawingCreateFromComponentsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewFusionDrawingDocumentCommand:
		ID = "NewFusionDrawingDocumentCommand"
		isNative = True
		class NewFusionDrawingDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewFusionDrawingTemplateCommand:
		ID = "NewFusionDrawingTemplateCommand"
		isNative = True
		class NewFusionDrawingTemplateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DashboardCreateFusionDrawingCommand:
		ID = "DashboardCreateFusionDrawingCommand"
		isNative = True
		class DashboardCreateFusionDrawingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ExportFusionDrawingDocumentCommand:
		ID = "ExportFusionDrawingDocumentCommand"
		isNative = True
		class ExportFusionDrawingDocumentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExportDXFCommand:
		ID = "FusionDrawingExportDXFCommand"
		isNative = True
		class FusionDrawingExportDXFCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExportPDFCommand:
		ID = "FusionDrawingExportPDFCommand"
		isNative = True
		class FusionDrawingExportPDFCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExportSinglePDFCommand:
		ID = "FusionDrawingExportSinglePDFCommand"
		isNative = True
		class FusionDrawingExportSinglePDFCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExportSelectedSheetsPDFCommand:
		ID = "FusionDrawingExportSelectedSheetsPDFCommand"
		isNative = True
		class FusionDrawingExportSelectedSheetsPDFCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExportFusionDrawingTemplateCommand:
		ID = "ExportFusionDrawingTemplateCommand"
		isNative = True
		class ExportFusionDrawingTemplateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExportPartsListCommand:
		ID = "FusionDrawingExportPartsListCommand"
		isNative = True
		class FusionDrawingExportPartsListCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingUndoCommand:
		ID = "FusionDrawingUndoCommand"
		isNative = True
		class FusionDrawingUndoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRedoCommand:
		ID = "FusionDrawingRedoCommand"
		isNative = True
		class FusionDrawingRedoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewBaseCommand:
		ID = "FusionDrawingViewBaseCommand"
		isNative = True
		class FusionDrawingViewBaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewBaseTemplateCommand:
		ID = "FusionDrawingViewBaseTemplateCommand"
		isNative = True
		class FusionDrawingViewBaseTemplateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewEditCommand:
		ID = "FusionDrawingViewEditCommand"
		isNative = True
		class FusionDrawingViewEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionBrokenViewCommand:
		ID = "FusionBrokenViewCommand"
		isNative = True
		class FusionBrokenViewCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionBrokenViewEditCommand:
		ID = "FusionBrokenViewEditCommand"
		isNative = True
		class FusionBrokenViewEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingLinearDimensionCmd:
		ID = "FusionDrawingLinearDimensionCmd"
		isNative = True
		class FusionDrawingLinearDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAlignedDimensionCmd:
		ID = "FusionDrawingAlignedDimensionCmd"
		isNative = True
		class FusionDrawingAlignedDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAngularDimensionCmd:
		ID = "FusionDrawingAngularDimensionCmd"
		isNative = True
		class FusionDrawingAngularDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRadialDimensionCmd:
		ID = "FusionDrawingRadialDimensionCmd"
		isNative = True
		class FusionDrawingRadialDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBaselineDimensionCmd:
		ID = "FusionDrawingBaselineDimensionCmd"
		isNative = True
		class FusionDrawingBaselineDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingChainDimensionCmd:
		ID = "FusionDrawingChainDimensionCmd"
		isNative = True
		class FusionDrawingChainDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingOrdinateDimensionCmd:
		ID = "FusionDrawingOrdinateDimensionCmd"
		isNative = True
		class FusionDrawingOrdinateDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingEdgeExtensionCmd:
		ID = "FusionDrawingEdgeExtensionCmd"
		isNative = True
		class FusionDrawingEdgeExtensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDimensionBreakCmd:
		ID = "FusionDrawingDimensionBreakCmd"
		isNative = True
		class FusionDrawingDimensionBreakCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAddDimensionBreakCmd:
		ID = "FusionDrawingAddDimensionBreakCmd"
		isNative = True
		class FusionDrawingAddDimensionBreakCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRemoveDimensionBreakCmd:
		ID = "FusionDrawingRemoveDimensionBreakCmd"
		isNative = True
		class FusionDrawingRemoveDimensionBreakCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingMTextCommand:
		ID = "FusionDrawingMTextCommand"
		isNative = True
		class FusionDrawingMTextCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingLeaderCommand:
		ID = "FusionDrawingLeaderCommand"
		isNative = True
		class FusionDrawingLeaderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBendNoteLeaderCommand:
		ID = "FusionDrawingBendNoteLeaderCommand"
		isNative = True
		class FusionDrawingBendNoteLeaderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingHoleThreadNoteLeaderCommand:
		ID = "FusionDrawingHoleThreadNoteLeaderCommand"
		isNative = True
		class FusionDrawingHoleThreadNoteLeaderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingNoteCommand:
		ID = "FusionDrawingNoteCommand"
		isNative = True
		class FusionDrawingNoteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingArrowCommand:
		ID = "FusionDrawingArrowCommand"
		isNative = True
		class FusionDrawingArrowCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTableCommand:
		ID = "FusionDrawingTableCommand"
		isNative = True
		class FusionDrawingTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTableTextEditCommand:
		ID = "FusionDrawingTableTextEditCommand"
		isNative = True
		class FusionDrawingTableTextEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTableEditCommand:
		ID = "FusionDrawingTableEditCommand"
		isNative = True
		class FusionDrawingTableEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCenterlineCommand:
		ID = "FusionDrawingCenterlineCommand"
		isNative = True
		class FusionDrawingCenterlineCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCentermarkCommand:
		ID = "FusionDrawingCentermarkCommand"
		isNative = True
		class FusionDrawingCentermarkCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCenterPatternCommand:
		ID = "FusionDrawingCenterPatternCommand"
		isNative = True
		class FusionDrawingCenterPatternCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCenterPatternEditCommand:
		ID = "FusionDrawingCenterPatternEditCommand"
		isNative = True
		class FusionDrawingCenterPatternEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDiameterDimensionCmd:
		ID = "FusionDrawingDiameterDimensionCmd"
		isNative = True
		class FusionDrawingDiameterDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSingleDimensionCmd:
		ID = "FusionDrawingSingleDimensionCmd"
		isNative = True
		class FusionDrawingSingleDimensionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewSimpleSectionCommand:
		ID = "FusionDrawingViewSimpleSectionCommand"
		isNative = True
		class FusionDrawingViewSimpleSectionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewSectionCommand:
		ID = "FusionDrawingViewSectionCommand"
		isNative = True
		class FusionDrawingViewSectionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewDetailCommand:
		ID = "FusionDrawingViewDetailCommand"
		isNative = True
		class FusionDrawingViewDetailCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewProjectCommand:
		ID = "FusionDrawingViewProjectCommand"
		isNative = True
		class FusionDrawingViewProjectCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingViewProjectTemplateCommand:
		ID = "FusionDrawingViewProjectTemplateCommand"
		isNative = True
		class FusionDrawingViewProjectTemplateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingMoveCmd:
		ID = "FusionDrawingMoveCmd"
		isNative = True
		class FusionDrawingMoveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocRotateCmd:
		ID = "FusionDocRotateCmd"
		isNative = True
		class FusionDocRotateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingHatchEditCmd:
		ID = "FusionDrawingHatchEditCmd"
		isNative = True
		class FusionDrawingHatchEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocRestoreDefaultsCmd:
		ID = "FusionDocRestoreDefaultsCmd"
		isNative = True
		class FusionDocRestoreDefaultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDimensionEditCmd:
		ID = "FusionDrawingDimensionEditCmd"
		isNative = True
		class FusionDrawingDimensionEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingEraseCmd:
		ID = "FusionDrawingEraseCmd"
		isNative = True
		class FusionDrawingEraseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocDeleteCmd:
		ID = "FusionDocDeleteCmd"
		isNative = True
		class FusionDocDeleteCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPanCmd:
		ID = "FusionDrawingPanCmd"
		isNative = True
		class FusionDrawingPanCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingZoomCmd:
		ID = "FusionDrawingZoomCmd"
		isNative = True
		class FusionDrawingZoomCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingFitCmd:
		ID = "FusionDrawingFitCmd"
		isNative = True
		class FusionDrawingFitCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDimReassociateCmd:
		ID = "FusionDrawingDimReassociateCmd"
		isNative = True
		class FusionDrawingDimReassociateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSmartObjReassociateCmd:
		ID = "FusionDrawingSmartObjReassociateCmd"
		isNative = True
		class FusionDrawingSmartObjReassociateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDisabledReassocCmd:
		ID = "FusionDrawingDisabledReassocCmd"
		isNative = True
		class FusionDrawingDisabledReassocCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCustomLeaderReassociateCmd:
		ID = "FusionDrawingCustomLeaderReassociateCmd"
		isNative = True
		class FusionDrawingCustomLeaderReassociateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingContinueCmd:
		ID = "FusionDrawingContinueCmd"
		isNative = True
		class FusionDrawingContinueCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTitleBlockEditCommand:
		ID = "FusionDrawingTitleBlockEditCommand"
		isNative = True
		class FusionDrawingTitleBlockEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCreatePartsListCommand:
		ID = "FusionDrawingCreatePartsListCommand"
		isNative = True
		class FusionDrawingCreatePartsListCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingNewTableCommand:
		ID = "FusionDrawingNewTableCommand"
		isNative = True
		class FusionDrawingNewTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingNewTableTemplateCommand:
		ID = "FusionDrawingNewTableTemplateCommand"
		isNative = True
		class FusionDrawingNewTableTemplateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingEmptyTableCommand:
		ID = "FusionDrawingEmptyTableCommand"
		isNative = True
		class FusionDrawingEmptyTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPartsListTableCommand:
		ID = "FusionDrawingPartsListTableCommand"
		isNative = True
		class FusionDrawingPartsListTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBendTableCommand:
		ID = "FusionDrawingBendTableCommand"
		isNative = True
		class FusionDrawingBendTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRevisionTableCommand:
		ID = "FusionDrawingRevisionTableCommand"
		isNative = True
		class FusionDrawingRevisionTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBendIDCommand:
		ID = "FusionDrawingBendIDCommand"
		isNative = True
		class FusionDrawingBendIDCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBalloonCommand:
		ID = "FusionDrawingBalloonCommand"
		isNative = True
		class FusionDrawingBalloonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSplineBalloonCommand:
		ID = "FusionDrawingSplineBalloonCommand"
		isNative = True
		class FusionDrawingSplineBalloonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRenumberCommand:
		ID = "FusionDrawingRenumberCommand"
		isNative = True
		class FusionDrawingRenumberCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAlignBalloonCommand:
		ID = "FusionDrawingAlignBalloonCommand"
		isNative = True
		class FusionDrawingAlignBalloonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAnnotationSettingsCmd:
		ID = "FusionDrawingAnnotationSettingsCmd"
		isNative = True
		class FusionDrawingAnnotationSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class FusionDrawingAnnotationFontCmd:
		ID = "FusionDrawingAnnotationFontCmd"
		isNative = True
	class FusionDrawingAnnotationTextHeightCmd:
		ID = "FusionDrawingAnnotationTextHeightCmd"
		isNative = True
	class FusionDrawingLinearUnitFormatCmd:
		ID = "FusionDrawingLinearUnitFormatCmd"
		isNative = True
	class FusionDrawingLinearDimensionPrecisionCmd:
		ID = "FusionDrawingLinearDimensionPrecisionCmd"
		isNative = True
	class FusionDrawingAngularDimensionPrecisionCmd:
		ID = "FusionDrawingAngularDimensionPrecisionCmd"
		isNative = True
	class FusionDrawingAnnotationUnitDisplayCmd:
		ID = "FusionDrawingAnnotationUnitDisplayCmd"
		isNative = True
		class FusionDrawingAnnotationUnitDisplayCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDrawingAnnotationTrailingZeroCmd:
		ID = "FusionDrawingAnnotationTrailingZeroCmd"
		isNative = True
		class FusionDrawingAnnotationTrailingZeroCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDrawingAnnotationLeadingZeroCmd:
		ID = "FusionDrawingAnnotationLeadingZeroCmd"
		isNative = True
		class FusionDrawingAnnotationLeadingZeroCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDrawingStandardCmd:
		ID = "FusionDrawingStandardCmd"
		isNative = True
		class FusionDrawingStandardCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAnnotationUnitCmd:
		ID = "FusionDrawingAnnotationUnitCmd"
		isNative = True
		class FusionDrawingAnnotationUnitCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingProjectionAngleCmd:
		ID = "FusionDrawingProjectionAngleCmd"
		isNative = True
		class FusionDrawingProjectionAngleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetSettingsCmd:
		ID = "FusionDrawingSheetSettingsCmd"
		isNative = True
		class FusionDrawingSheetSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class FusionDrawingSheetSizeCmd:
		ID = "FusionDrawingSheetSizeCmd"
		isNative = True
	class FusionDrawingTitleBlockCmd:
		ID = "FusionDrawingTitleBlockCmd"
		isNative = True
	class FusionDrawingTitleBlockDisplayCmd:
		ID = "FusionDrawingTitleBlockDisplayCmd"
		isNative = True
		class FusionDrawingTitleBlockDisplayCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDrawingBorderDisplayCmd:
		ID = "FusionDrawingBorderDisplayCmd"
		isNative = True
		class FusionDrawingBorderDisplayCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class FusionDrawingMTextEditCommand:
		ID = "FusionDrawingMTextEditCommand"
		isNative = True
		class FusionDrawingMTextEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingMLeaderContentEditCommand:
		ID = "FusionDrawingMLeaderContentEditCommand"
		isNative = True
		class FusionDrawingMLeaderContentEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingObjPropSettingsCmd:
		ID = "FusionDrawingObjPropSettingsCmd"
		isNative = True
		class FusionDrawingObjPropSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingGripStretchCommand:
		ID = "FusionDrawingGripStretchCommand"
		isNative = True
		class FusionDrawingGripStretchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocRevCloudCommand:
		ID = "FusionDocRevCloudCommand"
		isNative = True
		class FusionDocRevCloudCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingNewTitleBlockCommand:
		ID = "FusionDrawingNewTitleBlockCommand"
		isNative = True
		class FusionDrawingNewTitleBlockCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBlockEditCommand:
		ID = "FusionDrawingBlockEditCommand"
		isNative = True
		class FusionDrawingBlockEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBlockCloseCommand:
		ID = "FusionDrawingBlockCloseCommand"
		isNative = True
		class FusionDrawingBlockCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingLineCommand:
		ID = "FusionDrawingLineCommand"
		isNative = True
		class FusionDrawingLineCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCircleCommand:
		ID = "FusionDrawingCircleCommand"
		isNative = True
		class FusionDrawingCircleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCircleDiameterCommand:
		ID = "FusionDrawingCircleDiameterCommand"
		isNative = True
		class FusionDrawingCircleDiameterCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCircle2PointCommand:
		ID = "FusionDrawingCircle2PointCommand"
		isNative = True
		class FusionDrawingCircle2PointCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCircle3PointCommand:
		ID = "FusionDrawingCircle3PointCommand"
		isNative = True
		class FusionDrawingCircle3PointCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRectangleCommand:
		ID = "FusionDrawingRectangleCommand"
		isNative = True
		class FusionDrawingRectangleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingArcCommand:
		ID = "FusionDrawingArcCommand"
		isNative = True
		class FusionDrawingArcCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingArcCenterCommand:
		ID = "FusionDrawingArcCenterCommand"
		isNative = True
		class FusionDrawingArcCenterCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingArcTangentCommand:
		ID = "FusionDrawingArcTangentCommand"
		isNative = True
		class FusionDrawingArcTangentCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingEllipseCommand:
		ID = "FusionDrawingEllipseCommand"
		isNative = True
		class FusionDrawingEllipseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingCopyCommand:
		ID = "FusionDrawingCopyCommand"
		isNative = True
		class FusionDrawingCopyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingOffsetCommand:
		ID = "FusionDrawingOffsetCommand"
		isNative = True
		class FusionDrawingOffsetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTrimCommand:
		ID = "FusionDrawingTrimCommand"
		isNative = True
		class FusionDrawingTrimCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingExtendCommand:
		ID = "FusionDrawingExtendCommand"
		isNative = True
		class FusionDrawingExtendCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAttDefCommand:
		ID = "FusionDrawingAttDefCommand"
		isNative = True
		class FusionDrawingAttDefCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingAttEditCommand:
		ID = "FusionDrawingAttEditCommand"
		isNative = True
		class FusionDrawingAttEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingLegacyTextEditCommand:
		ID = "FusionDrawingLegacyTextEditCommand"
		isNative = True
		class FusionDrawingLegacyTextEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBorderEditCommand:
		ID = "FusionDrawingBorderEditCommand"
		isNative = True
		class FusionDrawingBorderEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBorderCloseCommand:
		ID = "FusionDrawingBorderCloseCommand"
		isNative = True
		class FusionDrawingBorderCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingMeasureCommand:
		ID = "FusionDrawingMeasureCommand"
		isNative = True
		class FusionDrawingMeasureCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDatumIdCmd:
		ID = "FusionDrawingDatumIdCmd"
		isNative = True
		class FusionDrawingDatumIdCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSymbolEditCmd:
		ID = "FusionDrawingSymbolEditCmd"
		isNative = True
		class FusionDrawingSymbolEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingFeatureControlFrameCmd:
		ID = "FusionDrawingFeatureControlFrameCmd"
		isNative = True
		class FusionDrawingFeatureControlFrameCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSurfaceTextureCmd:
		ID = "FusionDrawingSurfaceTextureCmd"
		isNative = True
		class FusionDrawingSurfaceTextureCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingWeldSymbolCmd:
		ID = "FusionDrawingWeldSymbolCmd"
		isNative = True
		class FusionDrawingWeldSymbolCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTaperSlopeSymbolCmd:
		ID = "FusionDrawingTaperSlopeSymbolCmd"
		isNative = True
		class FusionDrawingTaperSlopeSymbolCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocUpdateCommand:
		ID = "FusionDocUpdateCommand"
		isNative = True
		class FusionDocUpdateCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDocChooseVersionCommand:
		ID = "FusionDocChooseVersionCommand"
		isNative = True
		class FusionDocChooseVersionCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingShowHideCommand:
		ID = "FusionDrawingShowHideCommand"
		isNative = True
		class FusionDrawingShowHideCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSuppressUnsuppressCommand:
		ID = "FusionDrawingSuppressUnsuppressCommand"
		isNative = True
		class FusionDrawingSuppressUnsuppressCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSuppressCommand:
		ID = "FusionDrawingSuppressCommand"
		isNative = True
		class FusionDrawingSuppressCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingUnsuppressCommand:
		ID = "FusionDrawingUnsuppressCommand"
		isNative = True
		class FusionDrawingUnsuppressCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingShowAllCommand:
		ID = "FusionDrawingShowAllCommand"
		isNative = True
		class FusionDrawingShowAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingShowAllChildCommand:
		ID = "FusionDrawingShowAllChildCommand"
		isNative = True
		class FusionDrawingShowAllChildCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingUnsuppressAllCommand:
		ID = "FusionDrawingUnsuppressAllCommand"
		isNative = True
		class FusionDrawingUnsuppressAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingUnsuppressAllChildCommand:
		ID = "FusionDrawingUnsuppressAllChildCommand"
		isNative = True
		class FusionDrawingUnsuppressAllChildCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSuppressAllExceptSelectedCommand:
		ID = "FusionDrawingSuppressAllExceptSelectedCommand"
		isNative = True
		class FusionDrawingSuppressAllExceptSelectedCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocScreenshotCmd:
		ID = "FusionDocScreenshotCmd"
		isNative = True
		class FusionDocScreenshotCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenRelatedDesignCommand:
		ID = "OpenRelatedDesignCommand"
		isNative = True
		class OpenRelatedDesignCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSmartSheetCommand:
		ID = "FusionDrawingSmartSheetCommand"
		isNative = True
		class FusionDrawingSmartSheetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSmartDrawingCommand:
		ID = "FusionDrawingSmartDrawingCommand"
		isNative = True
		class FusionDrawingSmartDrawingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDocSettingCommand:
		ID = "FusionChangeDocSettingCommand"
		isNative = True
		class FusionChangeDocSettingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeMultiDocSettingCommand:
		ID = "FusionChangeMultiDocSettingCommand"
		isNative = True
		class FusionChangeMultiDocSettingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeTextHeightGroupCommand:
		ID = "FusionChangeTextHeightGroupCommand"
		isNative = True
		class FusionChangeTextHeightGroupCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeFontCommand:
		ID = "FusionChangeFontCommand"
		isNative = True
		class FusionChangeFontCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeLinearFormatCommand:
		ID = "FusionChangeLinearFormatCommand"
		isNative = True
		class FusionChangeLinearFormatCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeLinearPrecisionCommand:
		ID = "FusionChangeLinearPrecisionCommand"
		isNative = True
		class FusionChangeLinearPrecisionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeAngularPrecisionCommand:
		ID = "FusionChangeAngularPrecisionCommand"
		isNative = True
		class FusionChangeAngularPrecisionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayLeadingZeroCommand:
		ID = "FusionChangeDisplayLeadingZeroCommand"
		isNative = True
		class FusionChangeDisplayLeadingZeroCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayTrailingZeroCommand:
		ID = "FusionChangeDisplayTrailingZeroCommand"
		isNative = True
		class FusionChangeDisplayTrailingZeroCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayUnitsCommand:
		ID = "FusionChangeDisplayUnitsCommand"
		isNative = True
		class FusionChangeDisplayUnitsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeLineWidthGroupCommand:
		ID = "FusionChangeLineWidthGroupCommand"
		isNative = True
		class FusionChangeLineWidthGroupCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayLineWidthCommand:
		ID = "FusionChangeDisplayLineWidthCommand"
		isNative = True
		class FusionChangeDisplayLineWidthCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDimensionUnitsCommand:
		ID = "FusionChangeDimensionUnitsCommand"
		isNative = True
		class FusionChangeDimensionUnitsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeRevisionScopeCommand:
		ID = "FusionChangeRevisionScopeCommand"
		isNative = True
		class FusionChangeRevisionScopeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeSheetSettingCommand:
		ID = "FusionChangeSheetSettingCommand"
		isNative = True
		class FusionChangeSheetSettingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeMultiSheetSettingsCommand:
		ID = "FusionChangeMultiSheetSettingsCommand"
		isNative = True
		class FusionChangeMultiSheetSettingsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeSheetSizeCommand:
		ID = "FusionChangeSheetSizeCommand"
		isNative = True
		class FusionChangeSheetSizeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeTitleBlockCommand:
		ID = "FusionChangeTitleBlockCommand"
		isNative = True
		class FusionChangeTitleBlockCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayBorderCommand:
		ID = "FusionChangeDisplayBorderCommand"
		isNative = True
		class FusionChangeDisplayBorderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeDisplayTitleBlockCommand:
		ID = "FusionChangeDisplayTitleBlockCommand"
		isNative = True
		class FusionChangeDisplayTitleBlockCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeBorderVisibilityCommand:
		ID = "FusionChangeBorderVisibilityCommand"
		isNative = True
		class FusionChangeBorderVisibilityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionChangeTitleBlockVisibilityCommand:
		ID = "FusionChangeTitleBlockVisibilityCommand"
		isNative = True
		class FusionChangeTitleBlockVisibilityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionTitleBlockManagementCommand:
		ID = "FusionTitleBlockManagementCommand"
		isNative = True
		class FusionTitleBlockManagementCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionEditPropertiesCommand:
		ID = "FusionEditPropertiesCommand"
		isNative = True
		class FusionEditPropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionResetPropertiesCommand:
		ID = "FusionResetPropertiesCommand"
		isNative = True
		class FusionResetPropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRevMarkerCommand:
		ID = "FusionDrawingRevMarkerCommand"
		isNative = True
		class FusionDrawingRevMarkerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DrawingUndoCommand:
		ID = "DrawingUndoCommand"
		isNative = True
		class DrawingUndoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DrawingRedoCommand:
		ID = "DrawingRedoCommand"
		isNative = True
		class DrawingRedoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetNewCommand:
		ID = "FusionDrawingSheetNewCommand"
		isNative = True
		class FusionDrawingSheetNewCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetAddCommand:
		ID = "FusionDrawingSheetAddCommand"
		isNative = True
		class FusionDrawingSheetAddCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetActivateCommand:
		ID = "FusionDrawingSheetActivateCommand"
		isNative = True
		class FusionDrawingSheetActivateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetDeleteCommand:
		ID = "FusionDrawingSheetDeleteCommand"
		isNative = True
		class FusionDrawingSheetDeleteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingMultiSheetDeleteCommand:
		ID = "FusionDrawingMultiSheetDeleteCommand"
		isNative = True
		class FusionDrawingMultiSheetDeleteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetRenameCommand:
		ID = "FusionDrawingSheetRenameCommand"
		isNative = True
		class FusionDrawingSheetRenameCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSheetReorderCommand:
		ID = "FusionDrawingSheetReorderCommand"
		isNative = True
		class FusionDrawingSheetReorderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingDebugCommand:
		ID = "FusionDrawingDebugCommand"
		isNative = True
		class FusionDrawingDebugCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPrintCommand:
		ID = "FusionDrawingPrintCommand"
		isNative = True
		class FusionDrawingPrintCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPrintSingleSheetCommand:
		ID = "FusionDrawingPrintSingleSheetCommand"
		isNative = True
		class FusionDrawingPrintSingleSheetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPrintSelectedSheetsCommand:
		ID = "FusionDrawingPrintSelectedSheetsCommand"
		isNative = True
		class FusionDrawingPrintSelectedSheetsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingImageInsertCommand:
		ID = "FusionDrawingImageInsertCommand"
		isNative = True
		class FusionDrawingImageInsertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBlockEditorImageInsertCommand:
		ID = "FusionDrawingBlockEditorImageInsertCommand"
		isNative = True
		class FusionDrawingBlockEditorImageInsertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingTemplateImageInsertCommand:
		ID = "FusionDrawingTemplateImageInsertCommand"
		isNative = True
		class FusionDrawingTemplateImageInsertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingImageEditCommand:
		ID = "FusionDrawingImageEditCommand"
		isNative = True
		class FusionDrawingImageEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBlockRefEditCommand:
		ID = "FusionDrawingBlockRefEditCommand"
		isNative = True
		class FusionDrawingBlockRefEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingFeatureToggleCommand:
		ID = "FusionDrawingFeatureToggleCommand"
		isNative = True
		class FusionDrawingFeatureToggleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingPartsListEditCommand:
		ID = "FusionDrawingPartsListEditCommand"
		isNative = True
		class FusionDrawingPartsListEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBendTableEditCommand:
		ID = "FusionDrawingBendTableEditCommand"
		isNative = True
		class FusionDrawingBendTableEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingRevisionTableEditCommand:
		ID = "FusionDrawingRevisionTableEditCommand"
		isNative = True
		class FusionDrawingRevisionTableEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSketchCommand:
		ID = "FusionDrawingSketchCommand"
		isNative = True
		class FusionDrawingSketchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSketchCloseCommand:
		ID = "FusionDrawingSketchCloseCommand"
		isNative = True
		class FusionDrawingSketchCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SketchShowHideCommand:
		ID = "SketchShowHideCommand"
		isNative = True
		class SketchShowHideCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSketchRenameCommand:
		ID = "FusionDrawingSketchRenameCommand"
		isNative = True
		class FusionDrawingSketchRenameCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCutSketchCommand:
		ID = "FusionDocCutSketchCommand"
		isNative = True
		class FusionDocCutSketchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCopySketchCommand:
		ID = "FusionDocCopySketchCommand"
		isNative = True
		class FusionDocCopySketchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteSketchCommand:
		ID = "FusionDocPasteSketchCommand"
		isNative = True
		class FusionDocPasteSketchCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCopyMtextCommand:
		ID = "FusionDocCopyMtextCommand"
		isNative = True
		class FusionDocCopyMtextCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCutMtextCommand:
		ID = "FusionDocCutMtextCommand"
		isNative = True
		class FusionDocCutMtextCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteTextCommand:
		ID = "FusionDocPasteTextCommand"
		isNative = True
		class FusionDocPasteTextCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteCustomMTextCommand:
		ID = "FusionDocPasteCustomMTextCommand"
		isNative = True
		class FusionDocPasteCustomMTextCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteCustomTableCommand:
		ID = "FusionDocPasteCustomTableCommand"
		isNative = True
		class FusionDocPasteCustomTableCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCutGeomEntityCommand:
		ID = "FusionDocCutGeomEntityCommand"
		isNative = True
		class FusionDocCutGeomEntityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCopyGeomEntityCommand:
		ID = "FusionDocCopyGeomEntityCommand"
		isNative = True
		class FusionDocCopyGeomEntityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteGeomEntityCommand:
		ID = "FusionDocPasteGeomEntityCommand"
		isNative = True
		class FusionDocPasteGeomEntityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCutDefaultCommand:
		ID = "FusionDocCutDefaultCommand"
		isNative = True
		class FusionDocCutDefaultCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocCopyDefaultCommand:
		ID = "FusionDocCopyDefaultCommand"
		isNative = True
		class FusionDocCopyDefaultCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDocPasteDefaultCommand:
		ID = "FusionDocPasteDefaultCommand"
		isNative = True
		class FusionDocPasteDefaultCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSketchDeleteCommand:
		ID = "FusionDrawingSketchDeleteCommand"
		isNative = True
		class FusionDrawingSketchDeleteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingSketchEditCommand:
		ID = "FusionDrawingSketchEditCommand"
		isNative = True
		class FusionDrawingSketchEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditPaletteLinetypeCommand:
		ID = "EditPaletteLinetypeCommand"
		isNative = True
		class EditPaletteLinetypeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditPaletteLineweightCommand:
		ID = "EditPaletteLineweightCommand"
		isNative = True
		class EditPaletteLineweightCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePaletteOtherGeometryCommand:
		ID = "TogglePaletteOtherGeometryCommand"
		isNative = True
		class TogglePaletteOtherGeometryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePaletteSnapCommand:
		ID = "TogglePaletteSnapCommand"
		isNative = True
		class TogglePaletteSnapCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePaletteGridCommand:
		ID = "TogglePaletteGridCommand"
		isNative = True
		class TogglePaletteGridCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePaletteBorderCommand:
		ID = "TogglePaletteBorderCommand"
		isNative = True
		class TogglePaletteBorderCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePaletteSheetCommand:
		ID = "TogglePaletteSheetCommand"
		isNative = True
		class TogglePaletteSheetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingUpdateLinkTable:
		ID = "FusionDrawingUpdateLinkTable"
		isNative = True
		class FusionDrawingUpdateLinkTable_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDrawingBreakLinkTable:
		ID = "FusionDrawingBreakLinkTable"
		isNative = True
		class FusionDrawingBreakLinkTable_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherChangeZoomLevelCmd:
		ID = "PublisherChangeZoomLevelCmd"
		isNative = True
		class PublisherChangeZoomLevelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherChangeDescriptionCommand:
		ID = "PublisherChangeDescriptionCommand"
		isNative = True
		class PublisherChangeDescriptionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherActivateStoryboardCommand:
		ID = "PublisherActivateStoryboardCommand"
		isNative = True
		class PublisherActivateStoryboardCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RenameStoryboardCmd:
		ID = "RenameStoryboardCmd"
		isNative = True
		class RenameStoryboardCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherMoveComponentsCommand:
		ID = "PublisherMoveComponentsCommand"
		isNative = True
		class PublisherMoveComponentsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherRestoreHomeCommand:
		ID = "PublisherRestoreHomeCommand"
		isNative = True
		class PublisherRestoreHomeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherExplodeDirectChildrenCommand:
		ID = "PublisherExplodeDirectChildrenCommand"
		isNative = True
		class PublisherExplodeDirectChildrenCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherExplodeAllPartsCommand:
		ID = "PublisherExplodeAllPartsCommand"
		isNative = True
		class PublisherExplodeAllPartsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherManualExplodeCommand:
		ID = "PublisherManualExplodeCommand"
		isNative = True
		class PublisherManualExplodeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherDeleteCommand:
		ID = "PublisherDeleteCommand"
		isNative = True
		class PublisherDeleteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherDeleteActorCommand:
		ID = "PublisherDeleteActorCommand"
		isNative = True
		class PublisherDeleteActorCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherCopyCommand:
		ID = "PublisherCopyCommand"
		isNative = True
		class PublisherCopyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherPasteCommand:
		ID = "PublisherPasteCommand"
		isNative = True
		class PublisherPasteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherMoveSequenceEntryCommand:
		ID = "PublisherMoveSequenceEntryCommand"
		isNative = True
		class PublisherMoveSequenceEntryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherVisibilityToggleCmd:
		ID = "PublisherVisibilityToggleCmd"
		isNative = True
		class PublisherVisibilityToggleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherAppearanceCommand:
		ID = "PublisherAppearanceCommand"
		isNative = True
		class PublisherAppearanceCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherScopeMaterialCommand:
		ID = "PublisherScopeMaterialCommand"
		isNative = True
		class PublisherScopeMaterialCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherMaterialToggleCommand:
		ID = "PublisherMaterialToggleCommand"
		isNative = True
		class PublisherMaterialToggleCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherDurationCmd:
		ID = "PublisherDurationCmd"
		isNative = True
		class PublisherDurationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherEditActionCmd:
		ID = "PublisherEditActionCmd"
		isNative = True
		class PublisherEditActionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherEditSmartObjectActionCmd:
		ID = "PublisherEditSmartObjectActionCmd"
		isNative = True
		class PublisherEditSmartObjectActionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherCreateCameraActionCmd:
		ID = "PublisherCreateCameraActionCmd"
		isNative = True
		class PublisherCreateCameraActionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReverseSequenceEntryCmd:
		ID = "ReverseSequenceEntryCmd"
		isNative = True
		class ReverseSequenceEntryCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RenameStoryboardShellCmd:
		ID = "RenameStoryboardShellCmd"
		isNative = True
		class RenameStoryboardShellCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AlignActionStartTimesCmd:
		ID = "AlignActionStartTimesCmd"
		isNative = True
		class AlignActionStartTimesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AlignActionEndTimesCmd:
		ID = "AlignActionEndTimesCmd"
		isNative = True
		class AlignActionEndTimesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SelectAllAfterCmd:
		ID = "SelectAllAfterCmd"
		isNative = True
		class SelectAllAfterCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SelectAllBeforeCmd:
		ID = "SelectAllBeforeCmd"
		isNative = True
		class SelectAllBeforeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherChangeActionStartTimeCmd:
		ID = "PublisherChangeActionStartTimeCmd"
		isNative = True
		class PublisherChangeActionStartTimeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherChangeActionEndTimeCmd:
		ID = "PublisherChangeActionEndTimeCmd"
		isNative = True
		class PublisherChangeActionEndTimeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherMoveActionCmd:
		ID = "PublisherMoveActionCmd"
		isNative = True
		class PublisherMoveActionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherToggleCameraRecordingCmd:
		ID = "PublisherToggleCameraRecordingCmd"
		isNative = True
		class PublisherToggleCameraRecordingCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherExpandCompositeActionsCmd:
		ID = "PublisherExpandCompositeActionsCmd"
		isNative = True
		class PublisherExpandCompositeActionsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReorderActorCommand:
		ID = "ReorderActorCommand"
		isNative = True
		class ReorderActorCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExportVideoCommand:
		ID = "ExportVideoCommand"
		isNative = True
		class ExportVideoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherFindInBrowser:
		ID = "PublisherFindInBrowser"
		isNative = True
		class PublisherFindInBrowser_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherFindInWindow:
		ID = "PublisherFindInWindow"
		isNative = True
		class PublisherFindInWindow_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ApplicationSettingsEditCmd:
		ID = "ApplicationSettingsEditCmd"
		isNative = True
		class ApplicationSettingsEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherCreateStoryboardCommand:
		ID = "PublisherCreateStoryboardCommand"
		isNative = True
		class PublisherCreateStoryboardCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherEditTransformActionCommand:
		ID = "PublisherEditTransformActionCommand"
		isNative = True
		class PublisherEditTransformActionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherNewDrawingDocumentCommand:
		ID = "PublisherNewDrawingDocumentCommand"
		isNative = True
		class PublisherNewDrawingDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PublisherIsolateCmd:
		ID = "PublisherIsolateCmd"
		isNative = True
		class PublisherIsolateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherUnisolateCmd:
		ID = "PublisherUnisolateCmd"
		isNative = True
		class PublisherUnisolateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherCreateSelectionGroupCmd:
		ID = "PublisherCreateSelectionGroupCmd"
		isNative = True
		class PublisherCreateSelectionGroupCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LaunchScreencastCommand:
		ID = "LaunchScreencastCommand"
		isNative = True
		class LaunchScreencastCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSimulateInCFDCommand:
		ID = "FusionSimulateInCFDCommand"
		isNative = True
		class FusionSimulateInCFDCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionCFDModelAssessmentToolCommand:
		ID = "FusionCFDModelAssessmentToolCommand"
		isNative = True
		class FusionCFDModelAssessmentToolCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSimulateInCFD2020Command:
		ID = "FusionSimulateInCFD2020Command"
		isNative = True
		class FusionSimulateInCFD2020Command_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionCFD2020ModelAssessmentToolCommand:
		ID = "FusionCFD2020ModelAssessmentToolCommand"
		isNative = True
		class FusionCFD2020ModelAssessmentToolCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSimulateInCFD2021Command:
		ID = "FusionSimulateInCFD2021Command"
		isNative = True
		class FusionSimulateInCFD2021Command_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionCFD2021ModelAssessmentToolCommand:
		ID = "FusionCFD2021ModelAssessmentToolCommand"
		isNative = True
		class FusionCFD2021ModelAssessmentToolCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSimulateInMoldflowAdviserCommand:
		ID = "FusionSimulateInMoldflowAdviserCommand"
		isNative = True
		class FusionSimulateInMoldflowAdviserCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSimulateInMoldflowInsightCommand:
		ID = "FusionSimulateInMoldflowInsightCommand"
		isNative = True
		class FusionSimulateInMoldflowInsightCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetMetalRulesCommand:
		ID = "FusionSheetMetalRulesCommand"
		isNative = True
		class FusionSheetMetalRulesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetMetalFlangeCommand:
		ID = "FusionSheetMetalFlangeCommand"
		isNative = True
		class FusionSheetMetalFlangeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionBaseFaceEditCommand:
		ID = "FusionBaseFaceEditCommand"
		isNative = True
		class FusionBaseFaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SheetMetalBendCmd:
		ID = "SheetMetalBendCmd"
		isNative = True
		class SheetMetalBendCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SheetMetalBendEditCmd:
		ID = "SheetMetalBendEditCmd"
		isNative = True
		class SheetMetalBendEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConvertToSheetMetalCmd:
		ID = "ConvertToSheetMetalCmd"
		isNative = True
		class ConvertToSheetMetalCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DMConvertToSheetMetalCmd:
		ID = "DMConvertToSheetMetalCmd"
		isNative = True
		class DMConvertToSheetMetalCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ConvertToSheetMetalEditCmd:
		ID = "ConvertToSheetMetalEditCmd"
		isNative = True
		class ConvertToSheetMetalEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ChangeSheetMetalDataCommand:
		ID = "ChangeSheetMetalDataCommand"
		isNative = True
		class ChangeSheetMetalDataCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetmetalUnfoldCommand:
		ID = "FusionSheetmetalUnfoldCommand"
		isNative = True
		class FusionSheetmetalUnfoldCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SheetmetalEditUnfoldCommand:
		ID = "SheetmetalEditUnfoldCommand"
		isNative = True
		class SheetmetalEditUnfoldCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetmetalRefoldCommand:
		ID = "FusionSheetmetalRefoldCommand"
		isNative = True
		class FusionSheetmetalRefoldCommand_control:
			isVisible = False
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetMetalFlatPatternCmd:
		ID = "FusionSheetMetalFlatPatternCmd"
		isNative = True
		class FusionSheetMetalFlatPatternCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetMetalExitFlatPatternCmd:
		ID = "FusionSheetMetalExitFlatPatternCmd"
		isNative = True
		class FusionSheetMetalExitFlatPatternCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateFlatPatternCommand:
		ID = "UpdateFlatPatternCommand"
		isNative = True
		class UpdateFlatPatternCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateFlatPatternFromMainDesignCommand:
		ID = "UpdateFlatPatternFromMainDesignCommand"
		isNative = True
		class UpdateFlatPatternFromMainDesignCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class UpdateAllFlatPatternsCommand:
		ID = "UpdateAllFlatPatternsCommand"
		isNative = True
		class UpdateAllFlatPatternsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSheetMetalFlatPatternActivateCmd:
		ID = "FusionSheetMetalFlatPatternActivateCmd"
		isNative = True
		class FusionSheetMetalFlatPatternActivateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FlatPatternDXFExportCmd:
		ID = "FlatPatternDXFExportCmd"
		isNative = True
		class FlatPatternDXFExportCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfacePatchCommand:
		ID = "FusionSurfacePatchCommand"
		isNative = True
		class FusionSurfacePatchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfacePatchEditCommand:
		ID = "FusionSurfacePatchEditCommand"
		isNative = True
		class FusionSurfacePatchEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceOffsetEditCommand:
		ID = "FusionDcSurfaceOffsetEditCommand"
		isNative = True
		class FusionDcSurfaceOffsetEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceOffsetShellEditCommand:
		ID = "FusionDcSurfaceOffsetShellEditCommand"
		isNative = True
		class FusionDcSurfaceOffsetShellEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcMidSurfaceEditCommand:
		ID = "FusionDcMidSurfaceEditCommand"
		isNative = True
		class FusionDcMidSurfaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceShellEditCommand:
		ID = "FusionDcSurfaceShellEditCommand"
		isNative = True
		class FusionDcSurfaceShellEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceDeleteFaceEditCommand:
		ID = "FusionDcSurfaceDeleteFaceEditCommand"
		isNative = True
		class FusionDcSurfaceDeleteFaceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcReverseNormalEdit:
		ID = "FusionDcReverseNormalEdit"
		isNative = True
		class FusionDcReverseNormalEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceTrimEditCommand:
		ID = "FusionDcSurfaceTrimEditCommand"
		isNative = True
		class FusionDcSurfaceTrimEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceMergeCommand:
		ID = "FusionSurfaceMergeCommand"
		isNative = True
		class FusionSurfaceMergeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceDeleteFacesCommand:
		ID = "FusionSurfaceDeleteFacesCommand"
		isNative = True
		class FusionSurfaceDeleteFacesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceReverseNormalCommand:
		ID = "FusionSurfaceReverseNormalCommand"
		isNative = True
		class FusionSurfaceReverseNormalCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceTrimCommand:
		ID = "FusionSurfaceTrimCommand"
		isNative = True
		class FusionSurfaceTrimCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceStitchCommand:
		ID = "FusionSurfaceStitchCommand"
		isNative = True
		class FusionSurfaceStitchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceStitchEditCommand:
		ID = "FusionSurfaceStitchEditCommand"
		isNative = True
		class FusionSurfaceStitchEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceUnStitchCommand:
		ID = "FusionSurfaceUnStitchCommand"
		isNative = True
		class FusionSurfaceUnStitchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceUnStitchEditCommand:
		ID = "FusionSurfaceUnStitchEditCommand"
		isNative = True
		class FusionSurfaceUnStitchEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceOffsetCommand:
		ID = "FusionSurfaceOffsetCommand"
		isNative = True
		class FusionSurfaceOffsetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceRuledCommand:
		ID = "FusionSurfaceRuledCommand"
		isNative = True
		class FusionSurfaceRuledCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceRuledEditCommand:
		ID = "FusionDcSurfaceRuledEditCommand"
		isNative = True
		class FusionDcSurfaceRuledEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceUntrimCommand:
		ID = "FusionSurfaceUntrimCommand"
		isNative = True
		class FusionSurfaceUntrimCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionDcSurfaceUntrimEditCommand:
		ID = "FusionDcSurfaceUntrimEditCommand"
		isNative = True
		class FusionDcSurfaceUntrimEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceMidsurfaceShellCommand:
		ID = "FusionSurfaceMidsurfaceShellCommand"
		isNative = True
		class FusionSurfaceMidsurfaceShellCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceOffsetShellCommand:
		ID = "FusionSurfaceOffsetShellCommand"
		isNative = True
		class FusionSurfaceOffsetShellCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfaceShellConvertCommand:
		ID = "SurfaceShellConvertCommand"
		isNative = True
		class SurfaceShellConvertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceMidsurfaceShellEditCommand:
		ID = "FusionSurfaceMidsurfaceShellEditCommand"
		isNative = True
		class FusionSurfaceMidsurfaceShellEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceShellEditCommand:
		ID = "FusionSurfaceShellEditCommand"
		isNative = True
		class FusionSurfaceShellEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SurfaceRevolve:
		ID = "SurfaceRevolve"
		isNative = True
		class SurfaceRevolve_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SurfaceSweep:
		ID = "SurfaceSweep"
		isNative = True
		class SurfaceSweep_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceValidateCommand:
		ID = "FusionSurfaceValidateCommand"
		isNative = True
		class FusionSurfaceValidateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceTransparencyCommand:
		ID = "FusionSurfaceTransparencyCommand"
		isNative = True
		class FusionSurfaceTransparencyCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FusionSurfaceSelectionTransparencyCommand:
		ID = "FusionSurfaceSelectionTransparencyCommand"
		isNative = True
		class FusionSurfaceSelectionTransparencyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InsertMeshCommand:
		ID = "InsertMeshCommand"
		isNative = True
		class InsertMeshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Mesh2BRepCommand:
		ID = "Mesh2BRepCommand"
		isNative = True
		class Mesh2BRepCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class BRep2MeshCommand:
		ID = "BRep2MeshCommand"
		isNative = True
		class BRep2MeshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeshDeleteTrianglesCommand:
		ID = "MeshDeleteTrianglesCommand"
		isNative = True
		class MeshDeleteTrianglesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshSubsetCommand:
		ID = "MeshSubsetCommand"
		isNative = True
		class MeshSubsetCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshRemeshCommand:
		ID = "MeshRemeshCommand"
		isNative = True
		class MeshRemeshCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshReplaceCommand:
		ID = "MeshReplaceCommand"
		isNative = True
		class MeshReplaceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshReduceCommand:
		ID = "MeshReduceCommand"
		isNative = True
		class MeshReduceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshSmoothCommand:
		ID = "MeshSmoothCommand"
		isNative = True
		class MeshSmoothCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshCreateFGCommand:
		ID = "MeshCreateFGCommand"
		isNative = True
		class MeshCreateFGCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshClearFGCommand:
		ID = "MeshClearFGCommand"
		isNative = True
		class MeshClearFGCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshReverseNormalsCommand:
		ID = "MeshReverseNormalsCommand"
		isNative = True
		class MeshReverseNormalsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshGenerateFGCommand:
		ID = "MeshGenerateFGCommand"
		isNative = True
		class MeshGenerateFGCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshPlaneCutCommand:
		ID = "MeshPlaneCutCommand"
		isNative = True
		class MeshPlaneCutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshMakeSolidCommand:
		ID = "MeshMakeSolidCommand"
		isNative = True
		class MeshMakeSolidCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class MeshPlanarSectionCommand:
		ID = "MeshPlanarSectionCommand"
		isNative = True
		class MeshPlanarSectionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeshStyleCommand:
		ID = "MeshStyleCommand"
		isNative = True
		class MeshStyleCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxListControlDefinition"
	class MeshColorCommand:
		ID = "MeshColorCommand"
		isNative = True
	class MeshCombineCommand:
		ID = "MeshCombineCommand"
		isNative = True
		class MeshCombineCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class FlatMeshShadingCmd:
		ID = "FlatMeshShadingCmd"
		isNative = True
		class FlatMeshShadingCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SmoothMeshShadingCmd:
		ID = "SmoothMeshShadingCmd"
		isNative = True
		class SmoothMeshShadingCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class InsertAlignMeshCommand:
		ID = "InsertAlignMeshCommand"
		isNative = True
		class InsertAlignMeshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PositionMeshCommand:
		ID = "PositionMeshCommand"
		isNative = True
		class PositionMeshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeshTriangulateCommand:
		ID = "MeshTriangulateCommand"
		isNative = True
		class MeshTriangulateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBDefineBoardCmd:
		ID = "PCBDefineBoardCmd"
		isNative = True
		class PCBDefineBoardCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBImprintCmd:
		ID = "PCBImprintCmd"
		isNative = True
		class PCBImprintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBActivate:
		ID = "PCBActivate"
		isNative = True
		class PCBActivate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBStop:
		ID = "PCBStop"
		isNative = True
		class PCBStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBCreateCmd:
		ID = "PCBCreateCmd"
		isNative = True
		class PCBCreateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBDeriveCmd:
		ID = "PCBDeriveCmd"
		isNative = True
		class PCBDeriveCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBWorkspaceCmd:
		ID = "PCBWorkspaceCmd"
		isNative = True
		class PCBWorkspaceCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBStatusCmd:
		ID = "PCBStatusCmd"
		isNative = True
		class PCBStatusCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBMoveComponentsCmd:
		ID = "PCBMoveComponentsCmd"
		isNative = True
		class PCBMoveComponentsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBFlipComponentCmd:
		ID = "PCBFlipComponentCmd"
		isNative = True
		class PCBFlipComponentCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBNewDocumentCmd:
		ID = "PCBNewDocumentCmd"
		isNative = True
		class PCBNewDocumentCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PCBReplaceComponentCmd:
		ID = "PCBReplaceComponentCmd"
		isNative = True
		class PCBReplaceComponentCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBUpdateComponentCmd:
		ID = "PCBUpdateComponentCmd"
		isNative = True
		class PCBUpdateComponentCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBMoveComponentBodyCmd:
		ID = "PCBMoveComponentBodyCmd"
		isNative = True
		class PCBMoveComponentBodyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBBoardSketchEditCmd:
		ID = "PCBBoardSketchEditCmd"
		isNative = True
		class PCBBoardSketchEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCB3DFlipComponentCmd:
		ID = "PCB3DFlipComponentCmd"
		isNative = True
		class PCB3DFlipComponentCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCB3DMoveComponentsCmd:
		ID = "PCB3DMoveComponentsCmd"
		isNative = True
		class PCB3DMoveComponentsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBDocumentUpdateCmd:
		ID = "PCBDocumentUpdateCmd"
		isNative = True
		class PCBDocumentUpdateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBEditBoardCmd:
		ID = "PCBEditBoardCmd"
		isNative = True
		class PCBEditBoardCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCB3DBoardOutlineEditCommand:
		ID = "PCB3DBoardOutlineEditCommand"
		isNative = True
		class PCB3DBoardOutlineEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBHoleCmd:
		ID = "PCBHoleCmd"
		isNative = True
		class PCBHoleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBDcHoleEditCommand:
		ID = "PCBDcHoleEditCommand"
		isNative = True
		class PCBDcHoleEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CalloutCommand:
		ID = "CalloutCommand"
		isNative = True
		class CalloutCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DragCalloutCmd:
		ID = "DragCalloutCmd"
		isNative = True
		class DragCalloutCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CalloutEditCommand:
		ID = "CalloutEditCommand"
		isNative = True
		class CalloutEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherTrailVisibilityCommand:
		ID = "PublisherTrailVisibilityCommand"
		isNative = True
		class PublisherTrailVisibilityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherTrailShowAllCommand:
		ID = "PublisherTrailShowAllCommand"
		isNative = True
		class PublisherTrailShowAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PublisherTrailHideAllCommand:
		ID = "PublisherTrailHideAllCommand"
		isNative = True
		class PublisherTrailHideAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TrailDragCmd:
		ID = "TrailDragCmd"
		isNative = True
		class TrailDragCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPropertiesCommand:
		ID = "SimPropertiesCommand"
		isNative = True
		class SimPropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimActivateCmd:
		ID = "SimActivateCmd"
		isNative = True
		class SimActivateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDoubleClickCmdDef:
		ID = "SimDoubleClickCmdDef"
		isNative = True
		class SimDoubleClickCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditCmd:
		ID = "SimEditCmd"
		isNative = True
		class SimEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnitsSettingsCommand:
		ID = "SimUnitsSettingsCommand"
		isNative = True
		class SimUnitsSettingsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimVisibilityToggleCmd:
		ID = "SimVisibilityToggleCmd"
		isNative = True
		class SimVisibilityToggleCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnsuppressAllCommand:
		ID = "SimUnsuppressAllCommand"
		isNative = True
		class SimUnsuppressAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ToggleLearningPanelCmd:
		ID = "ToggleLearningPanelCmd"
		isNative = True
		class ToggleLearningPanelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateSimCaseCommand:
		ID = "SimCreateSimCaseCommand"
		isNative = True
		class SimCreateSimCaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateGenCaseCmd:
		ID = "SimCreateGenCaseCmd"
		isNative = True
		class SimCreateGenCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateGenCaseFluidsCmd:
		ID = "SimCreateGenCaseFluidsCmd"
		isNative = True
		class SimCreateGenCaseFluidsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateSimCaseFromGenerativeDesignCommand:
		ID = "SimCreateSimCaseFromGenerativeDesignCommand"
		isNative = True
		class SimCreateSimCaseFromGenerativeDesignCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreCommand:
		ID = "ExploreCommand"
		isNative = True
		class ExploreCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreFluidsCommand:
		ID = "ExploreFluidsCommand"
		isNative = True
		class ExploreFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreDisplayThumbnailViewCmd:
		ID = "ExploreDisplayThumbnailViewCmd"
		isNative = True
	class ExploreDisplayPropertiesViewCmd:
		ID = "ExploreDisplayPropertiesViewCmd"
		isNative = True
	class ExploreDisplayScatterPlotViewCmd:
		ID = "ExploreDisplayScatterPlotViewCmd"
		isNative = True
	class ExploreDisplayTableViewCmd:
		ID = "ExploreDisplayTableViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayModelViewCmd:
		ID = "ExploreOutcomeProfileDisplayModelViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayModelViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayModelViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayTransparentViewCmd:
		ID = "ExploreOutcomeProfileDisplayTransparentViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayTransparentViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayTransparentViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayStressViewCmd:
		ID = "ExploreOutcomeProfileDisplayStressViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayStressViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayStressViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayFlowLineViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayFlowLineViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayExportPreviewCmd:
		ID = "ExploreOutcomeProfileDisplayExportPreviewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayExportPreviewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayExportPreviewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayPreserveViewCmd:
		ID = "ExploreOutcomeProfileDisplayPreserveViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayPreserveViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayPreserveViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayObstacleViewCmd:
		ID = "ExploreOutcomeProfileDisplayObstacleViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayObstacleViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayObstacleViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayStartingShapeViewCmd:
		ID = "ExploreOutcomeProfileDisplayStartingShapeViewCmd"
		isNative = True
	class ExploreOutcomeProfileDisplayStartingShapeViewFluidsCmd:
		ID = "ExploreOutcomeProfileDisplayStartingShapeViewFluidsCmd"
		isNative = True
	class ExploreOutcomeProfileCompareCmd:
		ID = "ExploreOutcomeProfileCompareCmd"
		isNative = True
		class ExploreOutcomeProfileCompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileCompareFluidsCmd:
		ID = "ExploreOutcomeProfileCompareFluidsCmd"
		isNative = True
		class ExploreOutcomeProfileCompareFluidsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileCompareAddEnabledCmd:
		ID = "ExploreOutcomeProfileCompareAddEnabledCmd"
		isNative = True
		class ExploreOutcomeProfileCompareAddEnabledCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileCompareAddDisabledCmd:
		ID = "ExploreOutcomeProfileCompareAddDisabledCmd"
		isNative = True
		class ExploreOutcomeProfileCompareAddDisabledCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileExportSmtCmd:
		ID = "ExploreOutcomeProfileExportSmtCmd"
		isNative = True
		class ExploreOutcomeProfileExportSmtCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileExportSmtFluidsCmd:
		ID = "ExploreOutcomeProfileExportSmtFluidsCmd"
		isNative = True
		class ExploreOutcomeProfileExportSmtFluidsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileExportStlCmd:
		ID = "ExploreOutcomeProfileExportStlCmd"
		isNative = True
		class ExploreOutcomeProfileExportStlCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreOutcomeProfileExportStlFluidsCmd:
		ID = "ExploreOutcomeProfileExportStlFluidsCmd"
		isNative = True
		class ExploreOutcomeProfileExportStlFluidsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreFavoritesCmd:
		ID = "ExploreFavoritesCmd"
		isNative = True
		class ExploreFavoritesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreLabelsCmd:
		ID = "ExploreLabelsCmd"
		isNative = True
		class ExploreLabelsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExploreSaveCSVCmd:
		ID = "ExploreSaveCSVCmd"
		isNative = True
		class ExploreSaveCSVCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishExploreCmd:
		ID = "FinishExploreCmd"
		isNative = True
		class FinishExploreCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishOutcomeViewCmd:
		ID = "FinishOutcomeViewCmd"
		isNative = True
		class FinishOutcomeViewCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishHawkeyeCmd:
		ID = "FinishHawkeyeCmd"
		isNative = True
		class FinishHawkeyeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishDoraCmd:
		ID = "FinishDoraCmd"
		isNative = True
		class FinishDoraCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimActivateSimCaseCommand:
		ID = "SimActivateSimCaseCommand"
		isNative = True
		class SimActivateSimCaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExpandActiveSimCaseCommand:
		ID = "SimExpandActiveSimCaseCommand"
		isNative = True
		class SimExpandActiveSimCaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimActivateSimLoadCaseCmd:
		ID = "SimActivateSimLoadCaseCmd"
		isNative = True
		class SimActivateSimLoadCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateSimLoadCaseCmd:
		ID = "SimCreateSimLoadCaseCmd"
		isNative = True
		class SimCreateSimLoadCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDuplicateSimLoadCaseCmd:
		ID = "SimDuplicateSimLoadCaseCmd"
		isNative = True
		class SimDuplicateSimLoadCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCopySimCaseCommand:
		ID = "SimCopySimCaseCommand"
		isNative = True
		class SimCopySimCaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCasePropertiesCmd:
		ID = "SimCasePropertiesCmd"
		isNative = True
		class SimCasePropertiesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenCasePropertiesCmd:
		ID = "GenCasePropertiesCmd"
		isNative = True
		class GenCasePropertiesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDeleteSimCaseCommand:
		ID = "SimDeleteSimCaseCommand"
		isNative = True
		class SimDeleteSimCaseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMeshSettingsCmd:
		ID = "SimMeshSettingsCmd"
		isNative = True
		class SimMeshSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSolveSettingsCmd:
		ID = "SimSolveSettingsCmd"
		isNative = True
		class SimSolveSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConvergenceSettingsCmd:
		ID = "SimConvergenceSettingsCmd"
		isNative = True
		class SimConvergenceSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactsSettingsCmd:
		ID = "SimContactsSettingsCmd"
		isNative = True
		class SimContactsSettingsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAutoSolverContactsEnableCmd:
		ID = "SimAutoSolverContactsEnableCmd"
		isNative = True
		class SimAutoSolverContactsEnableCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAutoSolverContactsDisableCmd:
		ID = "SimAutoSolverContactsDisableCmd"
		isNative = True
		class SimAutoSolverContactsDisableCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimOverrideMaterialCommand:
		ID = "SimOverrideMaterialCommand"
		isNative = True
		class SimOverrideMaterialCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMaterialPropertiesCommand:
		ID = "SimMaterialPropertiesCommand"
		isNative = True
		class SimMaterialPropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMaterialEditCommand:
		ID = "SimMaterialEditCommand"
		isNative = True
		class SimMaterialEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenMaterialEditCommand:
		ID = "GenMaterialEditCommand"
		isNative = True
		class GenMaterialEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUpdateMaterialCommand:
		ID = "SimUpdateMaterialCommand"
		isNative = True
		class SimUpdateMaterialCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUpdateCommand:
		ID = "SimUpdateCommand"
		isNative = True
		class SimUpdateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimReconnectJobOrganizerCommand:
		ID = "SimReconnectJobOrganizerCommand"
		isNative = True
		class SimReconnectJobOrganizerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDisplayDOFViewCommand:
		ID = "SimDisplayDOFViewCommand"
		isNative = True
	class SimDisplayGroupsViewCommand:
		ID = "SimDisplayGroupsViewCommand"
		isNative = True
	class SimDisplayNormalViewCommand:
		ID = "SimDisplayNormalViewCommand"
		isNative = True
	class SimIsolateCommand:
		ID = "SimIsolateCommand"
		isNative = True
		class SimIsolateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnisolateCommand:
		ID = "SimUnisolateCommand"
		isNative = True
		class SimUnisolateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnisolateAllCommand:
		ID = "SimUnisolateAllCommand"
		isNative = True
		class SimUnisolateAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SwitchToFusionCommand:
		ID = "SwitchToFusionCommand"
		isNative = True
		class SwitchToFusionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimIsolateBodyCommand:
		ID = "SimIsolateBodyCommand"
		isNative = True
		class SimIsolateBodyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnisolateBodyCommand:
		ID = "SimUnisolateBodyCommand"
		isNative = True
		class SimUnisolateBodyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimHideCommand:
		ID = "SimHideCommand"
		isNative = True
		class SimHideCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowCommand:
		ID = "SimShowCommand"
		isNative = True
		class SimShowCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSurfaceTransparencyCmd:
		ID = "SimSurfaceTransparencyCmd"
		isNative = True
		class SimSurfaceTransparencyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowHideBodyCmd:
		ID = "ShowHideBodyCmd"
		isNative = True
		class ShowHideBodyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimVisibilityAllCommand:
		ID = "SimVisibilityAllCommand"
		isNative = True
		class SimVisibilityAllCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowAllComponentsCommand:
		ID = "SimShowAllComponentsCommand"
		isNative = True
		class SimShowAllComponentsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowAllBodiesCommand:
		ID = "SimShowAllBodiesCommand"
		isNative = True
		class SimShowAllBodiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSwitchToPostProcessingCommand:
		ID = "SimSwitchToPostProcessingCommand"
		isNative = True
	class SimSwitchToPreviewMeshCommand:
		ID = "SimSwitchToPreviewMeshCommand"
		isNative = True
	class SimDofColorsCmd:
		ID = "SimDofColorsCmd"
		isNative = True
		class SimDofColorsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowJobsDlgCmd:
		ID = "SimShowJobsDlgCmd"
		isNative = True
		class SimShowJobsDlgCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenShowJobsDlgCmd:
		ID = "GenShowJobsDlgCmd"
		isNative = True
		class GenShowJobsDlgCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSelectRelatedContactsCommand:
		ID = "SimSelectRelatedContactsCommand"
		isNative = True
		class SimSelectRelatedContactsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDeleteCommonCommand:
		ID = "SimDeleteCommonCommand"
		isNative = True
		class SimDeleteCommonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimRemoveRigidBodyTargetCommand:
		ID = "SimRemoveRigidBodyTargetCommand"
		isNative = True
		class SimRemoveRigidBodyTargetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCopyCommonCommand:
		ID = "SimCopyCommonCommand"
		isNative = True
		class SimCopyCommonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSuppressCommonCommand:
		ID = "SimSuppressCommonCommand"
		isNative = True
		class SimSuppressCommonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimUnsuppressCommonCommand:
		ID = "SimUnsuppressCommonCommand"
		isNative = True
		class SimUnsuppressCommonCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConvergencePlotCmd:
		ID = "SimConvergencePlotCmd"
		isNative = True
		class SimConvergencePlotCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimReportCmd:
		ID = "SimReportCmd"
		isNative = True
		class SimReportCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowLMVCmd:
		ID = "SimShowLMVCmd"
		isNative = True
		class SimShowLMVCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMeasureCommand:
		ID = "SimMeasureCommand"
		isNative = True
		class SimMeasureCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SimActivateCompareCmd:
		ID = "SimActivateCompareCmd"
		isNative = True
		class SimActivateCompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSyncCameraCmd:
		ID = "SimSyncCameraCmd"
		isNative = True
	class SimSelectBodiesBySizeCommand:
		ID = "SimSelectBodiesBySizeCommand"
		isNative = True
		class SimSelectBodiesBySizeCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SimSelectByInvertCommand:
		ID = "SimSelectByInvertCommand"
		isNative = True
		class SimSelectByInvertCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SimSelectByBoundaryCommand:
		ID = "SimSelectByBoundaryCommand"
		isNative = True
		class SimSelectByBoundaryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSelectAllOccurrencesCommand:
		ID = "SimSelectAllOccurrencesCommand"
		isNative = True
		class SimSelectAllOccurrencesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSelectSimilarOccurrencesCommand:
		ID = "SimSelectSimilarOccurrencesCommand"
		isNative = True
		class SimSelectSimilarOccurrencesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSelectByNameCommand:
		ID = "SimSelectByNameCommand"
		isNative = True
		class SimSelectByNameCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SimSwitchToFusionAndRunInterferencesCommand:
		ID = "SimSwitchToFusionAndRunInterferencesCommand"
		isNative = True
		class SimSwitchToFusionAndRunInterferencesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAttributesAlertCommand:
		ID = "SimAttributesAlertCommand"
		isNative = True
		class SimAttributesAlertCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowAttributesCommand:
		ID = "SimShowAttributesCommand"
		isNative = True
		class SimShowAttributesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenShowAttributesCommand:
		ID = "GenShowAttributesCommand"
		isNative = True
		class GenShowAttributesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExportToMechanicalCommand:
		ID = "SimExportToMechanicalCommand"
		isNative = True
		class SimExportToMechanicalCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExportToDiscoveryCommand:
		ID = "SimExportToDiscoveryCommand"
		isNative = True
		class SimExportToDiscoveryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExportToScalarisCommand:
		ID = "SimExportToScalarisCommand"
		isNative = True
		class SimExportToScalarisCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSolveDetailsCmd:
		ID = "SimSolveDetailsCmd"
		isNative = True
		class SimSolveDetailsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenGenerateDetailsCmd:
		ID = "GenGenerateDetailsCmd"
		isNative = True
		class GenGenerateDetailsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenHideGenerateDetailsCmd:
		ID = "GenHideGenerateDetailsCmd"
		isNative = True
		class GenHideGenerateDetailsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCloudCreditInfoCommand:
		ID = "SimCloudCreditInfoCommand"
		isNative = True
		class SimCloudCreditInfoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenCloudCreditInfoCommand:
		ID = "SimGenCloudCreditInfoCommand"
		isNative = True
		class SimGenCloudCreditInfoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGen7DayTrialInfoCommand:
		ID = "SimGen7DayTrialInfoCommand"
		isNative = True
		class SimGen7DayTrialInfoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEnablePreviewStudyCommand:
		ID = "SimEnablePreviewStudyCommand"
		isNative = True
		class SimEnablePreviewStudyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSuppressAppearanceCommand:
		ID = "SimSuppressAppearanceCommand"
		isNative = True
	class SimSolveLogCmd:
		ID = "SimSolveLogCmd"
		isNative = True
		class SimSolveLogCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditResultsLegendCmd:
		ID = "SimEditResultsLegendCmd"
		isNative = True
		class SimEditResultsLegendCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultLegendOptionsCmd:
		ID = "SimResultLegendOptionsCmd"
		isNative = True
		class SimResultLegendOptionsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultLegendOptionsHotspotCmd:
		ID = "SimResultLegendOptionsHotspotCmd"
		isNative = True
		class SimResultLegendOptionsHotspotCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultLegendCallChart1Cmd:
		ID = "SimResultLegendCallChart1Cmd"
		isNative = True
		class SimResultLegendCallChart1Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultLegendCallChart2Cmd:
		ID = "SimResultLegendCallChart2Cmd"
		isNative = True
		class SimResultLegendCallChart2Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultLegendCallChart3Cmd:
		ID = "SimResultLegendCallChart3Cmd"
		isNative = True
		class SimResultLegendCallChart3Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsLegendShowCmd:
		ID = "SimResultsLegendShowCmd"
		isNative = True
		class SimResultsLegendShowCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsLegendHideCmd:
		ID = "SimResultsLegendHideCmd"
		isNative = True
		class SimResultsLegendHideCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsLegendMinRefValueResetCmd:
		ID = "SimResultsLegendMinRefValueResetCmd"
		isNative = True
		class SimResultsLegendMinRefValueResetCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsLegendMaxRefValueResetCmd:
		ID = "SimResultsLegendMaxRefValueResetCmd"
		isNative = True
		class SimResultsLegendMaxRefValueResetCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultTypeCmd:
		ID = "SimResultTypeCmd"
		isNative = True
		class SimResultTypeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimResultTypeGroupCmd:
		ID = "SimResultTypeGroupCmd"
		isNative = True
		class SimResultTypeGroupCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimResultUnitsCmd:
		ID = "SimResultUnitsCmd"
		isNative = True
		class SimResultUnitsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimResultNodeAverageCmd:
		ID = "SimResultNodeAverageCmd"
		isNative = True
		class SimResultNodeAverageCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimLoadCaseCmd:
		ID = "SimLoadCaseCmd"
		isNative = True
		class SimLoadCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimDomainPoint1Cmd:
		ID = "SimDomainPoint1Cmd"
		isNative = True
		class SimDomainPoint1Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimDomainPoint2Cmd:
		ID = "SimDomainPoint2Cmd"
		isNative = True
		class SimDomainPoint2Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimDomainPoint3Cmd:
		ID = "SimDomainPoint3Cmd"
		isNative = True
		class SimDomainPoint3Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimDomainPointInterpolable1Cmd:
		ID = "SimDomainPointInterpolable1Cmd"
		isNative = True
	class SimDomainPointInterpolable2Cmd:
		ID = "SimDomainPointInterpolable2Cmd"
		isNative = True
	class SimDomainPointInterpolable3Cmd:
		ID = "SimDomainPointInterpolable3Cmd"
		isNative = True
	class SimResultsRecommendationsCmd:
		ID = "SimResultsRecommendationsCmd"
		isNative = True
		class SimResultsRecommendationsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsRecommendationsAutomaticallyShowCmd:
		ID = "SimResultsRecommendationsAutomaticallyShowCmd"
		isNative = True
		class SimResultsRecommendationsAutomaticallyShowCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultRecommendationsShowDesignCmd:
		ID = "SimResultRecommendationsShowDesignCmd"
		isNative = True
		class SimResultRecommendationsShowDesignCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultRecommendationsEditSafetyFactorCmd:
		ID = "SimResultRecommendationsEditSafetyFactorCmd"
		isNative = True
		class SimResultRecommendationsEditSafetyFactorCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultRecommendationsDeformationScaleCmdDefKey:
		ID = "SimResultRecommendationsDeformationScaleCmdDefKey"
		isNative = True
		class SimResultRecommendationsDeformationScaleCmdDefKey_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsLegendConfigurationCmd:
		ID = "SimResultsLegendConfigurationCmd"
		isNative = True
	class SimSyncRefValuesCmd:
		ID = "SimSyncRefValuesCmd"
		isNative = True
	class SimSyncResultTypeCmd:
		ID = "SimSyncResultTypeCmd"
		isNative = True
	class SimContourLinesCmd:
		ID = "SimContourLinesCmd"
		isNative = True
		class SimContourLinesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActiveSimCaseCommand:
		ID = "ActiveSimCaseCommand"
		isNative = True
	class SimToggleMeshCmd:
		ID = "SimToggleMeshCmd"
		isNative = True
	class SimToggleWireframeCmd:
		ID = "SimToggleWireframeCmd"
		isNative = True
	class SimDisplacementScaleNoneCmd:
		ID = "SimDisplacementScaleNoneCmd"
		isNative = True
	class SimDisplacementScaleActualCmd:
		ID = "SimDisplacementScaleActualCmd"
		isNative = True
	class SimDisplacementScaleSmallCmd:
		ID = "SimDisplacementScaleSmallCmd"
		isNative = True
	class SimDisplacementScaleNormalCmd:
		ID = "SimDisplacementScaleNormalCmd"
		isNative = True
	class SimDisplacementScaleLargeCmd:
		ID = "SimDisplacementScaleLargeCmd"
		isNative = True
	class SimDisplacementScaleLargestCmd:
		ID = "SimDisplacementScaleLargestCmd"
		isNative = True
	class SimMinMaxProbesCmd:
		ID = "SimMinMaxProbesCmd"
		isNative = True
		class SimMinMaxProbesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSurfaceProbesCmd:
		ID = "SimSurfaceProbesCmd"
		isNative = True
		class SimSurfaceProbesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowAllProbesCmd:
		ID = "SimShowAllProbesCmd"
		isNative = True
		class SimShowAllProbesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimHideAllProbesCmd:
		ID = "SimHideAllProbesCmd"
		isNative = True
		class SimHideAllProbesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimDeleteAllProbesCmd:
		ID = "SimDeleteAllProbesCmd"
		isNative = True
		class SimDeleteAllProbesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPointProbeCmd:
		ID = "SimPointProbeCmd"
		isNative = True
		class SimPointProbeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditPointProbeCmd:
		ID = "SimEditPointProbeCmd"
		isNative = True
		class SimEditPointProbeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPointProbeStartCreationCmd:
		ID = "SimPointProbeStartCreationCmd"
		isNative = True
		class SimPointProbeStartCreationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPointProbeCreateCmd:
		ID = "SimPointProbeCreateCmd"
		isNative = True
		class SimPointProbeCreateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimProbePropertiesCommand:
		ID = "SimProbePropertiesCommand"
		isNative = True
		class SimProbePropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPointProbeSelectionCmd:
		ID = "SimPointProbeSelectionCmd"
		isNative = True
		class SimPointProbeSelectionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimProbeDragCommand:
		ID = "SimProbeDragCommand"
		isNative = True
		class SimProbeDragCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAnimateCommand:
		ID = "SimAnimateCommand"
		isNative = True
		class SimAnimateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimClippingPlaneStartCreationCmd:
		ID = "SimClippingPlaneStartCreationCmd"
		isNative = True
		class SimClippingPlaneStartCreationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimClippingPlaneEditCmd:
		ID = "SimClippingPlaneEditCmd"
		isNative = True
		class SimClippingPlaneEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimClippingPlaneCreateCmd:
		ID = "SimClippingPlaneCreateCmd"
		isNative = True
		class SimClippingPlaneCreateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout2HCmd:
		ID = "SimLayout2HCmd"
		isNative = True
		class SimLayout2HCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout2VCmd:
		ID = "SimLayout2VCmd"
		isNative = True
		class SimLayout2VCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout1V2HCmd:
		ID = "SimLayout1V2HCmd"
		isNative = True
		class SimLayout1V2HCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout1H2VCmd:
		ID = "SimLayout1H2VCmd"
		isNative = True
		class SimLayout1H2VCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout2x2Cmd:
		ID = "SimLayout2x2Cmd"
		isNative = True
		class SimLayout2x2Cmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout1H3VCmd:
		ID = "SimLayout1H3VCmd"
		isNative = True
		class SimLayout1H3VCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLayout1V3HCmd:
		ID = "SimLayout1V3HCmd"
		isNative = True
		class SimLayout1V3HCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransResult2DPlotCmd:
		ID = "SimTransResult2DPlotCmd"
		isNative = True
		class SimTransResult2DPlotCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFinishCompareCmd:
		ID = "SimFinishCompareCmd"
		isNative = True
		class SimFinishCompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPromoteCmd:
		ID = "SimPromoteCmd"
		isNative = True
		class SimPromoteCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishResultsCmd:
		ID = "FinishResultsCmd"
		isNative = True
		class FinishResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimResultsCmd:
		ID = "SimResultsCmd"
		isNative = True
		class SimResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimActivateSimCaseForWorkingModelCommand:
		ID = "SimActivateSimCaseForWorkingModelCommand"
		isNative = True
		class SimActivateSimCaseForWorkingModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteSimulationModelWithSimCasesCommand:
		ID = "DeleteSimulationModelWithSimCasesCommand"
		isNative = True
		class DeleteSimulationModelWithSimCasesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteGenerativeModelWithSimCasesCommand:
		ID = "DeleteGenerativeModelWithSimCasesCommand"
		isNative = True
		class DeleteGenerativeModelWithSimCasesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CopyWorkingModelWithSimCasesCommand:
		ID = "CopyWorkingModelWithSimCasesCommand"
		isNative = True
		class CopyWorkingModelWithSimCasesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CopyGenWorkingModelWithSimCasesCommand:
		ID = "CopyGenWorkingModelWithSimCasesCommand"
		isNative = True
		class CopyGenWorkingModelWithSimCasesCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DeleteSelectionGroupCmd:
		ID = "DeleteSelectionGroupCmd"
		isNative = True
		class DeleteSelectionGroupCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SwitchToSimplifyCommand:
		ID = "SwitchToSimplifyCommand"
		isNative = True
		class SwitchToSimplifyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditModelCommand:
		ID = "EditModelCommand"
		isNative = True
		class EditModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditModelFluidsCommand:
		ID = "EditModelFluidsCommand"
		isNative = True
		class EditModelFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CreateSimulationModelCommand:
		ID = "CreateSimulationModelCommand"
		isNative = True
		class CreateSimulationModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CreateGenerativeModelCommand:
		ID = "CreateGenerativeModelCommand"
		isNative = True
		class CreateGenerativeModelCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimForceLoadCommand:
		ID = "SimForceLoadCommand"
		isNative = True
		class SimForceLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMomentLoadCommand:
		ID = "SimMomentLoadCommand"
		isNative = True
		class SimMomentLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimPressureLoadCommand:
		ID = "SimPressureLoadCommand"
		isNative = True
		class SimPressureLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimBearingLoadCommand:
		ID = "SimBearingLoadCommand"
		isNative = True
		class SimBearingLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimRemoteForceLoadCommand:
		ID = "SimRemoteForceLoadCommand"
		isNative = True
		class SimRemoteForceLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLoadsCommand:
		ID = "SimLoadsCommand"
		isNative = True
		class SimLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenLoadsCommand:
		ID = "GenLoadsCommand"
		isNative = True
		class GenLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGravityCommand:
		ID = "SimGravityCommand"
		isNative = True
		class SimGravityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenGravityCommand:
		ID = "GenGravityCommand"
		isNative = True
		class GenGravityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAngularBodyLoadCommand:
		ID = "SimAngularBodyLoadCommand"
		isNative = True
		class SimAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLinearBodyLoadCommand:
		ID = "SimLinearBodyLoadCommand"
		isNative = True
		class SimLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGravityActivateCommand:
		ID = "SimGravityActivateCommand"
		isNative = True
		class SimGravityActivateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGravityDeactivateCommand:
		ID = "SimGravityDeactivateCommand"
		isNative = True
		class SimGravityDeactivateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimNewConstraintCmd:
		ID = "SimNewConstraintCmd"
		isNative = True
		class SimNewConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenNewConstraintCmd:
		ID = "GenNewConstraintCmd"
		isNative = True
		class GenNewConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConstraintFixedCmd:
		ID = "SimConstraintFixedCmd"
		isNative = True
		class SimConstraintFixedCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConstraintPinnedCmd:
		ID = "SimConstraintPinnedCmd"
		isNative = True
		class SimConstraintPinnedCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConstraintFrictionlessCmd:
		ID = "SimConstraintFrictionlessCmd"
		isNative = True
		class SimConstraintFrictionlessCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConstraintPrescribedDisplacementCmd:
		ID = "SimConstraintPrescribedDisplacementCmd"
		isNative = True
		class SimConstraintPrescribedDisplacementCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFlowRateCommand:
		ID = "SimFlowRateCommand"
		isNative = True
		class SimFlowRateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFlowVelocityCommand:
		ID = "SimFlowVelocityCommand"
		isNative = True
		class SimFlowVelocityCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimRemoteMomentLoadCommand:
		ID = "SimRemoteMomentLoadCommand"
		isNative = True
		class SimRemoteMomentLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenFluidsInletCommand:
		ID = "GenFluidsInletCommand"
		isNative = True
		class GenFluidsInletCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimAutoPointMassCommand:
		ID = "SimAutoPointMassCommand"
		isNative = True
		class SimAutoPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditAutoPointMassCommand:
		ID = "SimEditAutoPointMassCommand"
		isNative = True
		class SimEditAutoPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimManualPointMassCommand:
		ID = "SimManualPointMassCommand"
		isNative = True
		class SimManualPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditManualPointMassCommand:
		ID = "SimEditManualPointMassCommand"
		isNative = True
		class SimEditManualPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenManualPointMassCommand:
		ID = "GenManualPointMassCommand"
		isNative = True
		class GenManualPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenEditManualPointMassCommand:
		ID = "GenEditManualPointMassCommand"
		isNative = True
		class GenEditManualPointMassCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditLoadsCommand:
		ID = "SimEditLoadsCommand"
		isNative = True
		class SimEditLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenEditLoadsCommand:
		ID = "GenEditLoadsCommand"
		isNative = True
		class GenEditLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditConstraintCmd:
		ID = "SimEditConstraintCmd"
		isNative = True
		class SimEditConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenEditConstraintCmd:
		ID = "GenEditConstraintCmd"
		isNative = True
		class GenEditConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditAngularBodyLoadCommand:
		ID = "SimEditAngularBodyLoadCommand"
		isNative = True
		class SimEditAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditLinearBodyLoadCommand:
		ID = "SimEditLinearBodyLoadCommand"
		isNative = True
		class SimEditLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientLoadsCommand:
		ID = "SimTransientLoadsCommand"
		isNative = True
		class SimTransientLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditLoadsCommand:
		ID = "SimTransientEditLoadsCommand"
		isNative = True
		class SimTransientEditLoadsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientForceLoadCommand:
		ID = "SimTransientForceLoadCommand"
		isNative = True
		class SimTransientForceLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientPressureLoadCommand:
		ID = "SimTransientPressureLoadCommand"
		isNative = True
		class SimTransientPressureLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientMomentLoadCommand:
		ID = "SimTransientMomentLoadCommand"
		isNative = True
		class SimTransientMomentLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientAngularBodyLoadCommand:
		ID = "SimTransientAngularBodyLoadCommand"
		isNative = True
		class SimTransientAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditAngularBodyLoadCommand:
		ID = "SimTransientEditAngularBodyLoadCommand"
		isNative = True
		class SimTransientEditAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientLinearBodyLoadCommand:
		ID = "SimTransientLinearBodyLoadCommand"
		isNative = True
		class SimTransientLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditLinearBodyLoadCommand:
		ID = "SimTransientEditLinearBodyLoadCommand"
		isNative = True
		class SimTransientEditLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientBaseExcitationCmd:
		ID = "SimTransientBaseExcitationCmd"
		isNative = True
		class SimTransientBaseExcitationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditBaseExcitationCmd:
		ID = "SimTransientEditBaseExcitationCmd"
		isNative = True
		class SimTransientEditBaseExcitationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientPrescribedConstraintCmd:
		ID = "SimTransientPrescribedConstraintCmd"
		isNative = True
		class SimTransientPrescribedConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditPrescribedConstraintCmd:
		ID = "SimTransientEditPrescribedConstraintCmd"
		isNative = True
		class SimTransientEditPrescribedConstraintCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientPrescribedRotationCmd:
		ID = "SimTransientPrescribedRotationCmd"
		isNative = True
		class SimTransientPrescribedRotationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditPrescribedRotationCmd:
		ID = "SimTransientEditPrescribedRotationCmd"
		isNative = True
		class SimTransientEditPrescribedRotationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientBearingLoadCommand:
		ID = "SimTransientBearingLoadCommand"
		isNative = True
		class SimTransientBearingLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientRemoteForceLoadCommand:
		ID = "SimTransientRemoteForceLoadCommand"
		isNative = True
		class SimTransientRemoteForceLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientInitialAngularBodyLoadCommand:
		ID = "SimTransientInitialAngularBodyLoadCommand"
		isNative = True
		class SimTransientInitialAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditInitialAngularBodyLoadCommand:
		ID = "SimTransientEditInitialAngularBodyLoadCommand"
		isNative = True
		class SimTransientEditInitialAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientInitialLinearBodyLoadCommand:
		ID = "SimTransientInitialLinearBodyLoadCommand"
		isNative = True
		class SimTransientInitialLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTransientEditInitialLinearBodyLoadCommand:
		ID = "SimTransientEditInitialLinearBodyLoadCommand"
		isNative = True
		class SimTransientEditInitialLinearBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExplicitInitialAngularBodyLoadCommand:
		ID = "SimExplicitInitialAngularBodyLoadCommand"
		isNative = True
		class SimExplicitInitialAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExplicitEditInitialAngularBodyLoadCommand:
		ID = "SimExplicitEditInitialAngularBodyLoadCommand"
		isNative = True
		class SimExplicitEditInitialAngularBodyLoadCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConnectorBoltCommand:
		ID = "SimConnectorBoltCommand"
		isNative = True
		class SimConnectorBoltCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditConnectorBoltCommand:
		ID = "SimEditConnectorBoltCommand"
		isNative = True
		class SimEditConnectorBoltCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConnectorRigidBodyCommand:
		ID = "SimConnectorRigidBodyCommand"
		isNative = True
		class SimConnectorRigidBodyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditConnectorRigidBodyCommand:
		ID = "SimEditConnectorRigidBodyCommand"
		isNative = True
		class SimEditConnectorRigidBodyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimConnectorSpringCommand:
		ID = "SimConnectorSpringCommand"
		isNative = True
		class SimConnectorSpringCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditConnectorSpringCommand:
		ID = "SimEditConnectorSpringCommand"
		isNative = True
		class SimEditConnectorSpringCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenEditFluidsInletCommand:
		ID = "GenEditFluidsInletCommand"
		isNative = True
		class GenEditFluidsInletCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimNewPreserveBoundaryCmd:
		ID = "SimNewPreserveBoundaryCmd"
		isNative = True
		class SimNewPreserveBoundaryCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimNewSymmetryPlaneCmd:
		ID = "SimNewSymmetryPlaneCmd"
		isNative = True
		class SimNewSymmetryPlaneCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTopologyTargetCommand:
		ID = "SimTopologyTargetCommand"
		isNative = True
		class SimTopologyTargetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSeedTargetCommand:
		ID = "SimGenerativeSeedTargetCommand"
		isNative = True
		class SimGenerativeSeedTargetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSeedTargetFluidsCommand:
		ID = "SimGenerativeSeedTargetFluidsCommand"
		isNative = True
		class SimGenerativeSeedTargetFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeKeepBoundaryCommand:
		ID = "SimGenerativeKeepBoundaryCommand"
		isNative = True
		class SimGenerativeKeepBoundaryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeKeepBoundaryFluidsCommand:
		ID = "SimGenerativeKeepBoundaryFluidsCommand"
		isNative = True
		class SimGenerativeKeepBoundaryFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObstacleBoundaryCommand:
		ID = "SimGenerativeObstacleBoundaryCommand"
		isNative = True
		class SimGenerativeObstacleBoundaryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObstacleBoundaryFluidsCommand:
		ID = "SimGenerativeObstacleBoundaryFluidsCommand"
		isNative = True
		class SimGenerativeObstacleBoundaryFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditPreserveBoundaryCmd:
		ID = "SimEditPreserveBoundaryCmd"
		isNative = True
		class SimEditPreserveBoundaryCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditSymmetryPlaneCmd:
		ID = "SimEditSymmetryPlaneCmd"
		isNative = True
		class SimEditSymmetryPlaneCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSymmetryPlanesBoundaryCommand:
		ID = "SimGenerativeSymmetryPlanesBoundaryCommand"
		isNative = True
		class SimGenerativeSymmetryPlanesBoundaryCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSymmetryPreservePlanesHighlightCommand:
		ID = "SimGenerativeSymmetryPreservePlanesHighlightCommand"
		isNative = True
		class SimGenerativeSymmetryPreservePlanesHighlightCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSymmetryTopologyPlanesHighlightCommand:
		ID = "SimGenerativeSymmetryTopologyPlanesHighlightCommand"
		isNative = True
		class SimGenerativeSymmetryTopologyPlanesHighlightCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeSymmetryObstaclePlanesHighlightCommand:
		ID = "SimGenerativeSymmetryObstaclePlanesHighlightCommand"
		isNative = True
		class SimGenerativeSymmetryObstaclePlanesHighlightCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObstacleOffsetCommand:
		ID = "SimGenerativeObstacleOffsetCommand"
		isNative = True
		class SimGenerativeObstacleOffsetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObstacleOffsetFluidsCommand:
		ID = "SimGenerativeObstacleOffsetFluidsCommand"
		isNative = True
		class SimGenerativeObstacleOffsetFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeEditObstacleOffsetCommand:
		ID = "SimGenerativeEditObstacleOffsetCommand"
		isNative = True
		class SimGenerativeEditObstacleOffsetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObstacleInterferesPreserveHighlightCmd:
		ID = "SimGenerativeObstacleInterferesPreserveHighlightCmd"
		isNative = True
		class SimGenerativeObstacleInterferesPreserveHighlightCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditRigidTargetCommand:
		ID = "SimEditRigidTargetCommand"
		isNative = True
		class SimEditRigidTargetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimRigidTargetCommand:
		ID = "SimRigidTargetCommand"
		isNative = True
		class SimRigidTargetCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadsCmd:
		ID = "SimThermalLoadsCmd"
		isNative = True
		class SimThermalLoadsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadsEditCmd:
		ID = "SimThermalLoadsEditCmd"
		isNative = True
		class SimThermalLoadsEditCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadSurfaceHeatCmd:
		ID = "SimThermalLoadSurfaceHeatCmd"
		isNative = True
		class SimThermalLoadSurfaceHeatCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadInternalHeatCmd:
		ID = "SimThermalLoadInternalHeatCmd"
		isNative = True
		class SimThermalLoadInternalHeatCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadConvectionCmd:
		ID = "SimThermalLoadConvectionCmd"
		isNative = True
		class SimThermalLoadConvectionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadEmissivityCmd:
		ID = "SimThermalLoadEmissivityCmd"
		isNative = True
		class SimThermalLoadEmissivityCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalLoadTemperatureCmd:
		ID = "SimThermalLoadTemperatureCmd"
		isNative = True
		class SimThermalLoadTemperatureCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalGraphCmd:
		ID = "SimThermalGraphCmd"
		isNative = True
		class SimThermalGraphCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSPreSolveCheckCmd:
		ID = "SimFEACSPreSolveCheckCmd"
		isNative = True
		class SimFEACSPreSolveCheckCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenFEACSPreSolveCheckCmd:
		ID = "GenFEACSPreSolveCheckCmd"
		isNative = True
		class GenFEACSPreSolveCheckCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSDataCheckCmd:
		ID = "SimFEACSDataCheckCmd"
		isNative = True
		class SimFEACSDataCheckCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSMeshSolveCmd:
		ID = "SimFEACSMeshSolveCmd"
		isNative = True
		class SimFEACSMeshSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSMeshCloudSolveCmd:
		ID = "SimFEACSMeshCloudSolveCmd"
		isNative = True
		class SimFEACSMeshCloudSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSSolveCmd:
		ID = "SimFEACSSolveCmd"
		isNative = True
		class SimFEACSSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSEditSolveCmd:
		ID = "SimFEACSEditSolveCmd"
		isNative = True
		class SimFEACSEditSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSCloudSolveCmd:
		ID = "SimFEACSCloudSolveCmd"
		isNative = True
		class SimFEACSCloudSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSTopologyOptimizationSolveCmd:
		ID = "SimFEACSTopologyOptimizationSolveCmd"
		isNative = True
		class SimFEACSTopologyOptimizationSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSTopologyOptimizationSynchronousSolveCmd:
		ID = "SimFEACSTopologyOptimizationSynchronousSolveCmd"
		isNative = True
		class SimFEACSTopologyOptimizationSynchronousSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimSolveCmd:
		ID = "SimSolveCmd"
		isNative = True
		class SimSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenSolveCmd:
		ID = "GenSolveCmd"
		isNative = True
		class GenSolveCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GenSolveFluidsCmd:
		ID = "GenSolveFluidsCmd"
		isNative = True
		class GenSolveFluidsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSSolveAutoContactsCmd:
		ID = "SimFEACSSolveAutoContactsCmd"
		isNative = True
		class SimFEACSSolveAutoContactsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimManualContactCommand:
		ID = "SimManualContactCommand"
		isNative = True
		class SimManualContactCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSAutoContactsCmd:
		ID = "SimFEACSAutoContactsCmd"
		isNative = True
		class SimFEACSAutoContactsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditContactCommand:
		ID = "SimEditContactCommand"
		isNative = True
		class SimEditContactCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFlipContactRefsCommand:
		ID = "SimFlipContactRefsCommand"
		isNative = True
		class SimFlipContactRefsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactBondedCommand:
		ID = "SimContactBondedCommand"
		isNative = True
		class SimContactBondedCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactSeparationSlidingCommand:
		ID = "SimContactSeparationSlidingCommand"
		isNative = True
		class SimContactSeparationSlidingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactSeparationNoSlidingCommand:
		ID = "SimContactSeparationNoSlidingCommand"
		isNative = True
		class SimContactSeparationNoSlidingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactSlidingNoSeparationCommand:
		ID = "SimContactSlidingNoSeparationCommand"
		isNative = True
		class SimContactSlidingNoSeparationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactOffsetBondedCommand:
		ID = "SimContactOffsetBondedCommand"
		isNative = True
		class SimContactOffsetBondedCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCreateFatigueCaseCmd:
		ID = "SimCreateFatigueCaseCmd"
		isNative = True
		class SimCreateFatigueCaseCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCaseSettingCmd:
		ID = "SimFatigueCaseSettingCmd"
		isNative = True
		class SimFatigueCaseSettingCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCaseCloneCmd:
		ID = "SimFatigueCaseCloneCmd"
		isNative = True
		class SimFatigueCaseCloneCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCaseActivateCmd:
		ID = "SimFatigueCaseActivateCmd"
		isNative = True
		class SimFatigueCaseActivateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCaseOvMaterialCmd:
		ID = "SimFatigueCaseOvMaterialCmd"
		isNative = True
		class SimFatigueCaseOvMaterialCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCaseSurfaceFinishCmd:
		ID = "SimFatigueCaseSurfaceFinishCmd"
		isNative = True
		class SimFatigueCaseSurfaceFinishCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCycleHistoryCmd:
		ID = "SimFatigueCycleHistoryCmd"
		isNative = True
		class SimFatigueCycleHistoryCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueOutputOptCmd:
		ID = "SimFatigueOutputOptCmd"
		isNative = True
		class SimFatigueOutputOptCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueMaterialViewCmd:
		ID = "SimFatigueMaterialViewCmd"
		isNative = True
		class SimFatigueMaterialViewCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueCalcOptCmd:
		ID = "SimFatigueCalcOptCmd"
		isNative = True
		class SimFatigueCalcOptCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueSuppressPartCmd:
		ID = "SimFatigueSuppressPartCmd"
		isNative = True
		class SimFatigueSuppressPartCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueDeleteLinkedStudyCmd:
		ID = "SimFatigueDeleteLinkedStudyCmd"
		isNative = True
		class SimFatigueDeleteLinkedStudyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueEditLinkedStudiesCmd:
		ID = "SimFatigueEditLinkedStudiesCmd"
		isNative = True
		class SimFatigueEditLinkedStudiesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFatigueUpdateMaterialCmd:
		ID = "SimFatigueUpdateMaterialCmd"
		isNative = True
		class SimFatigueUpdateMaterialCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimShowMeshingIssuesCmd:
		ID = "SimShowMeshingIssuesCmd"
		isNative = True
		class SimShowMeshingIssuesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimHideMeshingIssuesCmd:
		ID = "SimHideMeshingIssuesCmd"
		isNative = True
		class SimHideMeshingIssuesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFEACSReactionForceCmd:
		ID = "SimFEACSReactionForceCmd"
		isNative = True
		class SimFEACSReactionForceCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimMeshRefinementByEntitiesCmd:
		ID = "SimMeshRefinementByEntitiesCmd"
		isNative = True
		class SimMeshRefinementByEntitiesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditMeshRefinementByEntitiesCmd:
		ID = "SimEditMeshRefinementByEntitiesCmd"
		isNative = True
		class SimEditMeshRefinementByEntitiesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimOptimizationSetupCommand:
		ID = "SimOptimizationSetupCommand"
		isNative = True
		class SimOptimizationSetupCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimOptimizationSetupEditCommand:
		ID = "SimOptimizationSetupEditCommand"
		isNative = True
		class SimOptimizationSetupEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimContactsManagerCmd:
		ID = "SimContactsManagerCmd"
		isNative = True
		class SimContactsManagerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimProgressBarUpdateCmdDef:
		ID = "SimProgressBarUpdateCmdDef"
		isNative = True
		class SimProgressBarUpdateCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObjectivesCommand:
		ID = "SimGenerativeObjectivesCommand"
		isNative = True
		class SimGenerativeObjectivesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeObjectivesFluidsCommand:
		ID = "SimGenerativeObjectivesFluidsCommand"
		isNative = True
		class SimGenerativeObjectivesFluidsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditGenerativeObjectivesCommand:
		ID = "SimEditGenerativeObjectivesCommand"
		isNative = True
		class SimEditGenerativeObjectivesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeManufacturingCommand:
		ID = "SimGenerativeManufacturingCommand"
		isNative = True
		class SimGenerativeManufacturingCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativePreviewCmd:
		ID = "SimGenerativePreviewCmd"
		isNative = True
		class SimGenerativePreviewCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGlobalAnalysisSpecificContactsCommand:
		ID = "SimGlobalAnalysisSpecificContactsCommand"
		isNative = True
		class SimGlobalAnalysisSpecificContactsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExplicitElementDeletionCommand:
		ID = "SimExplicitElementDeletionCommand"
		isNative = True
		class SimExplicitElementDeletionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditExplicitElementDeletionCommand:
		ID = "SimEditExplicitElementDeletionCommand"
		isNative = True
		class SimEditExplicitElementDeletionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFDInternalHeatAttributeCommand:
		ID = "SimFDInternalHeatAttributeCommand"
		isNative = True
		class SimFDInternalHeatAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFDEditInternalHeatAttributeCommand:
		ID = "SimFDEditInternalHeatAttributeCommand"
		isNative = True
		class SimFDEditInternalHeatAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimHeatSinkAttributeCommand:
		ID = "SimHeatSinkAttributeCommand"
		isNative = True
		class SimHeatSinkAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditHeatSinkAttributeCommand:
		ID = "SimEditHeatSinkAttributeCommand"
		isNative = True
		class SimEditHeatSinkAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimForcedFlowAttributeCommand:
		ID = "SimForcedFlowAttributeCommand"
		isNative = True
		class SimForcedFlowAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditForcedFlowAttributeCommand:
		ID = "SimEditForcedFlowAttributeCommand"
		isNative = True
		class SimEditForcedFlowAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFluidDynamicsWebViewerCmd:
		ID = "SimFluidDynamicsWebViewerCmd"
		isNative = True
		class SimFluidDynamicsWebViewerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimCriticalTemperaturesCommand:
		ID = "SimCriticalTemperaturesCommand"
		isNative = True
		class SimCriticalTemperaturesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFDRiskScaleCommand:
		ID = "SimFDRiskScaleCommand"
		isNative = True
	class SimFDSectionModeCommand:
		ID = "SimFDSectionModeCommand"
		isNative = True
	class SimFDTemperatureScaleCommand:
		ID = "SimFDTemperatureScaleCommand"
		isNative = True
	class StudyMaterialsCommand:
		ID = "StudyMaterialsCommand"
		isNative = True
		class StudyMaterialsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MaterialPropertiesCommand:
		ID = "MaterialPropertiesCommand"
		isNative = True
		class MaterialPropertiesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InjectionPointCommand:
		ID = "InjectionPointCommand"
		isNative = True
		class InjectionPointCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InjectionPointEditCommand:
		ID = "InjectionPointEditCommand"
		isNative = True
		class InjectionPointEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ViewResultsCommand:
		ID = "ViewResultsCommand"
		isNative = True
		class ViewResultsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InjectionMoldingSolveCommand:
		ID = "InjectionMoldingSolveCommand"
		isNative = True
		class InjectionMoldingSolveCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InjectionMoldingPreSolveCheckCommand:
		ID = "InjectionMoldingPreSolveCheckCommand"
		isNative = True
		class InjectionMoldingPreSolveCheckCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WebViewerCmd:
		ID = "WebViewerCmd"
		isNative = True
		class WebViewerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InjectionBodyCommand:
		ID = "InjectionBodyCommand"
		isNative = True
		class InjectionBodyCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class VisualFacesCommand:
		ID = "VisualFacesCommand"
		isNative = True
		class VisualFacesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ProcessSettingsCommand:
		ID = "ProcessSettingsCommand"
		isNative = True
		class ProcessSettingsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SummaryCardCommand:
		ID = "SummaryCardCommand"
		isNative = True
		class SummaryCardCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class CompareCommand:
		ID = "CompareCommand"
		isNative = True
	class Layout2HCommand:
		ID = "Layout2HCommand"
		isNative = True
		class Layout2HCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout2VCommand:
		ID = "Layout2VCommand"
		isNative = True
		class Layout2VCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout1V2HCommand:
		ID = "Layout1V2HCommand"
		isNative = True
		class Layout1V2HCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout1H2VCommand:
		ID = "Layout1H2VCommand"
		isNative = True
		class Layout1H2VCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout2x2Command:
		ID = "Layout2x2Command"
		isNative = True
		class Layout2x2Command_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout1H3VCommand:
		ID = "Layout1H3VCommand"
		isNative = True
		class Layout1H3VCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Layout1V3HCommand:
		ID = "Layout1V3HCommand"
		isNative = True
		class Layout1V3HCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CameraSyncCommand:
		ID = "CameraSyncCommand"
		isNative = True
	class FinishCompareCmd:
		ID = "FinishCompareCmd"
		isNative = True
		class FinishCompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FlatnessCommand:
		ID = "FlatnessCommand"
		isNative = True
	class SurfaceRoughnessCommand:
		ID = "SurfaceRoughnessCommand"
		isNative = True
	class IMSurfaceProbesCommand:
		ID = "IMSurfaceProbesCommand"
		isNative = True
	class IMShowAllProbesCommand:
		ID = "IMShowAllProbesCommand"
		isNative = True
		class IMShowAllProbesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IMHideAllProbesCommand:
		ID = "IMHideAllProbesCommand"
		isNative = True
		class IMHideAllProbesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IMDeleteAllProbesCommand:
		ID = "IMDeleteAllProbesCommand"
		isNative = True
		class IMDeleteAllProbesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CuttingPlaneCommand:
		ID = "CuttingPlaneCommand"
		isNative = True
		class CuttingPlaneCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DoraUndoCommand:
		ID = "DoraUndoCommand"
		isNative = True
		class DoraUndoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class DoraRedoCommand:
		ID = "DoraRedoCommand"
		isNative = True
		class DoraRedoCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class SimMassParticipationCommand:
		ID = "SimMassParticipationCommand"
		isNative = True
		class SimMassParticipationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGlobalExplicitContactsCommand:
		ID = "SimGlobalExplicitContactsCommand"
		isNative = True
		class SimGlobalExplicitContactsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimEditContactPairCommand:
		ID = "SimEditContactPairCommand"
		isNative = True
		class SimEditContactPairCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExplicitContactsManagerCommand:
		ID = "SimExplicitContactsManagerCommand"
		isNative = True
		class SimExplicitContactsManagerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeStudyMaterialsCommand:
		ID = "SimGenerativeStudyMaterialsCommand"
		isNative = True
		class SimGenerativeStudyMaterialsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimGenerativeFluidMaterialCommand:
		ID = "SimGenerativeFluidMaterialCommand"
		isNative = True
		class SimGenerativeFluidMaterialCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimBucklingResultsCmd:
		ID = "SimBucklingResultsCmd"
		isNative = True
		class SimBucklingResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimExplicitResultsCmd:
		ID = "SimExplicitResultsCmd"
		isNative = True
		class SimExplicitResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimLSSResultsCmd:
		ID = "SimLSSResultsCmd"
		isNative = True
		class SimLSSResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimModalResultsCmd:
		ID = "SimModalResultsCmd"
		isNative = True
		class SimModalResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimNLSSResultsCmd:
		ID = "SimNLSSResultsCmd"
		isNative = True
		class SimNLSSResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTopOptResultsCmd:
		ID = "SimTopOptResultsCmd"
		isNative = True
		class SimTopOptResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTemplateReusedAttributeCommand:
		ID = "SimTemplateReusedAttributeCommand"
		isNative = True
		class SimTemplateReusedAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTemplateStructuralAttributeCommand:
		ID = "SimTemplateStructuralAttributeCommand"
		isNative = True
		class SimTemplateStructuralAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTemplateEditStructuralAttributeCommand:
		ID = "SimTemplateEditStructuralAttributeCommand"
		isNative = True
		class SimTemplateEditStructuralAttributeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimTemplateWebViewerCmd:
		ID = "SimTemplateWebViewerCmd"
		isNative = True
		class SimTemplateWebViewerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimFinishTemplateWebViewerCmd:
		ID = "SimFinishTemplateWebViewerCmd"
		isNative = True
		class SimFinishTemplateWebViewerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalSteadyResultsCmd:
		ID = "SimThermalSteadyResultsCmd"
		isNative = True
		class SimThermalSteadyResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalStressReferenceTemperatureCommand:
		ID = "SimThermalStressReferenceTemperatureCommand"
		isNative = True
		class SimThermalStressReferenceTemperatureCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimThermalStressResultsCmd:
		ID = "SimThermalStressResultsCmd"
		isNative = True
		class SimThermalStressResultsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActivateMfgWorkingModelCmd:
		ID = "ActivateMfgWorkingModelCmd"
		isNative = True
		class ActivateMfgWorkingModelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteMfgWorkingModelCmd:
		ID = "DeleteMfgWorkingModelCmd"
		isNative = True
		class DeleteMfgWorkingModelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DuplicateMfgWorkingModelCmd:
		ID = "DuplicateMfgWorkingModelCmd"
		isNative = True
		class DuplicateMfgWorkingModelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdCreateWorkingModel:
		ID = "MSFWmdCreateWorkingModel"
		isNative = True
		class MSFWmdCreateWorkingModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CreateMfgWorkingModelFromDesignCmd:
		ID = "CreateMfgWorkingModelFromDesignCmd"
		isNative = True
		class CreateMfgWorkingModelFromDesignCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FinishPrepareWorkingModelCmd:
		ID = "FinishPrepareWorkingModelCmd"
		isNative = True
		class FinishPrepareWorkingModelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class InitializeAggregationCommand:
		ID = "InitializeAggregationCommand"
		isNative = True
		class InitializeAggregationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdAggregateFilesCmd:
		ID = "MSFWmdAggregateFilesCmd"
		isNative = True
		class MSFWmdAggregateFilesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateAggregationCommand:
		ID = "UpdateAggregationCommand"
		isNative = True
		class UpdateAggregationCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReferenceManagerCmd:
		ID = "ReferenceManagerCmd"
		isNative = True
		class ReferenceManagerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class OpenFileFromUrnCmd:
		ID = "OpenFileFromUrnCmd"
		isNative = True
		class OpenFileFromUrnCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MfgGetLatestCmd:
		ID = "MfgGetLatestCmd"
		isNative = True
		class MfgGetLatestCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdComponentLibraryCmd:
		ID = "MSFWmdComponentLibraryCmd"
		isNative = True
		class MSFWmdComponentLibraryCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdAddComponentInstanceCmd:
		ID = "MSFWmdAddComponentInstanceCmd"
		isNative = True
		class MSFWmdAddComponentInstanceCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdCompManagerCmd:
		ID = "MSFWmdCompManagerCmd"
		isNative = True
		class MSFWmdCompManagerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFWmdCreateAggregationAssetWorkingModelCmd:
		ID = "MSFWmdCreateAggregationAssetWorkingModelCmd"
		isNative = True
		class MSFWmdCreateAggregationAssetWorkingModelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DeleteMfgWorkingModelsCmd:
		ID = "DeleteMfgWorkingModelsCmd"
		isNative = True
		class DeleteMfgWorkingModelsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveSimulation:
		ID = "IronAdditiveSimulation"
		isNative = True
		class IronAdditiveSimulation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveBuildStrategy:
		ID = "IronAdditiveBuildStrategy"
		isNative = True
		class IronAdditiveBuildStrategy_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveExportStrategy:
		ID = "IronAdditiveExportStrategy"
		isNative = True
		class IronAdditiveExportStrategy_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronExportToolpath:
		ID = "IronExportToolpath"
		isNative = True
		class IronExportToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Iron3MFExport:
		ID = "Iron3MFExport"
		isNative = True
		class Iron3MFExport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFormlabsExport:
		ID = "IronFormlabsExport"
		isNative = True
		class IronFormlabsExport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveImportGCode:
		ID = "IronAdditiveImportGCode"
		isNative = True
		class IronAdditiveImportGCode_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveShowPrintStatistics:
		ID = "IronAdditiveShowPrintStatistics"
		isNative = True
		class IronAdditiveShowPrintStatistics_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class AdditiveResultsStop:
		ID = "AdditiveResultsStop"
		isNative = True
		class AdditiveResultsStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveExportCompensated:
		ID = "IronAdditiveExportCompensated"
		isNative = True
		class IronAdditiveExportCompensated_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveExportCompensatedSTL:
		ID = "IronAdditiveExportCompensatedSTL"
		isNative = True
		class IronAdditiveExportCompensatedSTL_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveMeshView:
		ID = "IronAdditiveMeshView"
		isNative = True
		class IronAdditiveMeshView_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveOpenResultsFolder:
		ID = "IronAdditiveOpenResultsFolder"
		isNative = True
		class IronAdditiveOpenResultsFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimMesh:
		ID = "IronAdditiveProcessSimMesh"
		isNative = True
		class IronAdditiveProcessSimMesh_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimPreCheck:
		ID = "IronAdditiveProcessSimPreCheck"
		isNative = True
		class IronAdditiveProcessSimPreCheck_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimulation:
		ID = "IronAdditiveProcessSimulation"
		isNative = True
		class IronAdditiveProcessSimulation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimSolve:
		ID = "IronAdditiveProcessSimSolve"
		isNative = True
		class IronAdditiveProcessSimSolve_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimToggleEdges:
		ID = "IronAdditiveProcessSimToggleEdges"
		isNative = True
		class IronAdditiveProcessSimToggleEdges_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveProcessSimMinMaxProbe:
		ID = "IronAdditiveProcessSimMinMaxProbe"
		isNative = True
		class IronAdditiveProcessSimMinMaxProbe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveResultsView:
		ID = "IronAdditiveResultsView"
		isNative = True
		class IronAdditiveResultsView_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveEditPrintSetting:
		ID = "IronAdditiveEditPrintSetting"
		isNative = True
		class IronAdditiveEditPrintSetting_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFFFInfillCmd:
		ID = "IronFFFInfillCmd"
		isNative = True
		class IronFFFInfillCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFFFSupportsCmd:
		ID = "IronFFFSupportsCmd"
		isNative = True
		class IronFFFSupportsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineSelection:
		ID = "MachineSelection"
		isNative = True
		class MachineSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SimplePrintSettingSelection:
		ID = "SimplePrintSettingSelection"
		isNative = True
		class SimplePrintSettingSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFlatPatternVisibility:
		ID = "IronFlatPatternVisibility"
		isNative = True
		class IronFlatPatternVisibility_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAddToNewFolder:
		ID = "IronAddToNewFolder"
		isNative = True
		class IronAddToNewFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAssociateNamedView:
		ID = "IronAssociateNamedView"
		isNative = True
		class IronAssociateNamedView_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAutomaticIPSGeneration:
		ID = "IronAutomaticIPSGeneration"
		isNative = True
		class IronAutomaticIPSGeneration_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCreateSelectionGroupCmd:
		ID = "IronCreateSelectionGroupCmd"
		isNative = True
		class IronCreateSelectionGroupCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFindInBrowser:
		ID = "IronFindInBrowser"
		isNative = True
		class IronFindInBrowser_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPasteCommand:
		ID = "IronPasteCommand"
		isNative = True
		class IronPasteCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMShowAllBodiesCmdDef:
		ID = "CAMShowAllBodiesCmdDef"
		isNative = True
		class CAMShowAllBodiesCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMShowAllComponentsCmdDef:
		ID = "CAMShowAllComponentsCmdDef"
		isNative = True
		class CAMShowAllComponentsCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMTechPreview:
		ID = "CAMTechPreview"
		isNative = True
		class CAMTechPreview_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMVisibilityToggleCmdDef:
		ID = "CAMVisibilityToggleCmdDef"
		isNative = True
		class CAMVisibilityToggleCmdDef_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronClearToolpath:
		ID = "IronClearToolpath"
		isNative = True
		class IronClearToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCollapseAllChildren:
		ID = "IronCollapseAllChildren"
		isNative = True
		class IronCollapseAllChildren_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCompareAndEdit:
		ID = "IronCompareAndEdit"
		isNative = True
		class IronCompareAndEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCopy:
		ID = "IronCopy"
		isNative = True
		class IronCopy_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CreateCAMModel:
		ID = "CreateCAMModel"
		isNative = True
		class CreateCAMModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCreateFromTemplate:
		ID = "IronCreateFromTemplate"
		isNative = True
		class IronCreateFromTemplate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCreateInspections:
		ID = "IronCreateInspections"
		isNative = True
		class IronCreateInspections_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditInspections:
		ID = "IronEditInspections"
		isNative = True
		class IronEditInspections_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCut:
		ID = "IronCut"
		isNative = True
		class IronCut_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDefaultFolder:
		ID = "IronDefaultFolder"
		isNative = True
		class IronDefaultFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDeleteObject:
		ID = "IronDeleteObject"
		isNative = True
		class IronDeleteObject_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDeleteEditSubToolpath:
		ID = "IronDeleteEditSubToolpath"
		isNative = True
		class IronDeleteEditSubToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDiscardEdits:
		ID = "IronDiscardEdits"
		isNative = True
		class IronDiscardEdits_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class DisplayAlignedResults:
		ID = "DisplayAlignedResults"
		isNative = True
		class DisplayAlignedResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDrawAllToolpathOps:
		ID = "IronDrawAllToolpathOps"
		isNative = True
		class IronDrawAllToolpathOps_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDrawAllToolpathsInParent:
		ID = "IronDrawAllToolpathsInParent"
		isNative = True
		class IronDrawAllToolpathsInParent_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDuplicate:
		ID = "IronDuplicate"
		isNative = True
		class IronDuplicate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditNotes:
		ID = "IronEditNotes"
		isNative = True
		class IronEditNotes_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditTool:
		ID = "IronEditTool"
		isNative = True
		class IronEditTool_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditWorkingModelSetup:
		ID = "IronEditWorkingModelSetup"
		isNative = True
		class IronEditWorkingModelSetup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronExpandAllChildren:
		ID = "IronExpandAllChildren"
		isNative = True
		class IronExpandAllChildren_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronExportDefaults:
		ID = "IronExportDefaults"
		isNative = True
		class IronExportDefaults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronExtractEditSubToolpath:
		ID = "IronExtractEditSubToolpath"
		isNative = True
		class IronExtractEditSubToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronGenerateStock:
		ID = "IronGenerateStock"
		isNative = True
		class IronGenerateStock_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronGenerateToolpath:
		ID = "IronGenerateToolpath"
		isNative = True
		class IronGenerateToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GeometrySelection:
		ID = "GeometrySelection"
		isNative = True
		class GeometrySelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GrabWidget:
		ID = "GrabWidget"
		isNative = True
		class GrabWidget_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideWarnings:
		ID = "HideWarnings"
		isNative = True
		class HideWarnings_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IronHoleRecognition:
		ID = "IronHoleRecognition"
		isNative = True
		class IronHoleRecognition_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditHoleRecognition:
		ID = "IronEditHoleRecognition"
		isNative = True
		class IronEditHoleRecognition_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronImportDefaults:
		ID = "IronImportDefaults"
		isNative = True
		class IronImportDefaults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ImportResults:
		ID = "ImportResults"
		isNative = True
		class ImportResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronInspectionReport:
		ID = "IronInspectionReport"
		isNative = True
		class IronInspectionReport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronIsolateCmd:
		ID = "IronIsolateCmd"
		isNative = True
		class IronIsolateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronKeepUpToDate:
		ID = "IronKeepUpToDate"
		isNative = True
		class IronKeepUpToDate_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class LiveProbing:
		ID = "LiveProbing"
		isNative = True
		class LiveProbing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LivePartAlignment:
		ID = "LivePartAlignment"
		isNative = True
		class LivePartAlignment_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMachineBrowser:
		ID = "IronMachineBrowser"
		isNative = True
		class IronMachineBrowser_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMachineBrowserSelection:
		ID = "IronMachineBrowserSelection"
		isNative = True
		class IronMachineBrowserSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMachineConfiguration:
		ID = "IronMachineConfiguration"
		isNative = True
		class IronMachineConfiguration_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMachineLibrary:
		ID = "IronMachineLibrary"
		isNative = True
		class IronMachineLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMachineVisibility:
		ID = "IronMachineVisibility"
		isNative = True
		class IronMachineVisibility_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class IronShowMachine:
		ID = "IronShowMachine"
		isNative = True
	class IronMachineTransparency:
		ID = "IronMachineTransparency"
		isNative = True
	class IronMachiningTime:
		ID = "IronMachiningTime"
		isNative = True
		class IronMachiningTime_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMakeAllDefault:
		ID = "IronMakeAllDefault"
		isNative = True
		class IronMakeAllDefault_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeasureDatum:
		ID = "MeasureDatum"
		isNative = True
		class MeasureDatum_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MeasureSurface:
		ID = "MeasureSurface"
		isNative = True
		class MeasureSurface_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MockDevice:
		ID = "MockDevice"
		isNative = True
		class MockDevice_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMoveInsertMarkerHere:
		ID = "IronMoveInsertMarkerHere"
		isNative = True
		class IronMoveInsertMarkerHere_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMoveInsertMarkerToEnd:
		ID = "IronMoveInsertMarkerToEnd"
		isNative = True
		class IronMoveInsertMarkerToEnd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronNcProgram:
		ID = "IronNcProgram"
		isNative = True
		class IronNcProgram_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditNcProgram:
		ID = "IronEditNcProgram"
		isNative = True
		class IronEditNcProgram_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronFolder:
		ID = "IronFolder"
		isNative = True
		class IronFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronOpenNcFolder:
		ID = "IronOpenNcFolder"
		isNative = True
		class IronOpenNcFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronOptional:
		ID = "IronOptional"
		isNative = True
		class IronOptional_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_IronStrategy_inspectSurface:
		ID = "PartAlignment_IronStrategy_inspectSurface"
		isNative = True
		class PartAlignment_IronStrategy_inspectSurface_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_EditAlignment:
		ID = "PartAlignment_EditAlignment"
		isNative = True
		class PartAlignment_EditAlignment_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_IronNcProgram:
		ID = "PartAlignment_IronNcProgram"
		isNative = True
		class PartAlignment_IronNcProgram_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_ImportResults:
		ID = "PartAlignment_ImportResults"
		isNative = True
		class PartAlignment_ImportResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_IronPartAlignmentInfo:
		ID = "PartAlignment_IronPartAlignmentInfo"
		isNative = True
		class PartAlignment_IronPartAlignmentInfo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignment_IronShowResults:
		ID = "PartAlignment_IronShowResults"
		isNative = True
		class PartAlignment_IronShowResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentPostStop:
		ID = "PartAlignmentPostStop"
		isNative = True
		class PartAlignmentPostStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentPostLive:
		ID = "PartAlignmentPostLive"
		isNative = True
		class PartAlignmentPostLive_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentStart_Delayed:
		ID = "PartAlignmentStart_Delayed"
		isNative = True
		class PartAlignmentStart_Delayed_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentStart_Live:
		ID = "PartAlignmentStart_Live"
		isNative = True
		class PartAlignmentStart_Live_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentStop_Delayed:
		ID = "PartAlignmentStop_Delayed"
		isNative = True
		class PartAlignmentStop_Delayed_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PartAlignmentStop_Live:
		ID = "PartAlignmentStop_Live"
		isNative = True
		class PartAlignmentStop_Live_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPostLibrary:
		ID = "IronPostLibrary"
		isNative = True
		class IronPostLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPostProcess:
		ID = "IronPostProcess"
		isNative = True
		class IronPostProcess_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPrintSettingLibrary:
		ID = "IronPrintSettingLibrary"
		isNative = True
		class IronPrintSettingLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronProtect:
		ID = "IronProtect"
		isNative = True
		class IronProtect_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IronPublishSetupSheet:
		ID = "IronPublishSetupSheet"
		isNative = True
		class IronPublishSetupSheet_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronRecalculateInspectionResults:
		ID = "IronRecalculateInspectionResults"
		isNative = True
		class IronRecalculateInspectionResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronRecordManualMeasure:
		ID = "IronRecordManualMeasure"
		isNative = True
		class IronRecordManualMeasure_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronReplayManualMeasure:
		ID = "IronReplayManualMeasure"
		isNative = True
		class IronReplayManualMeasure_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronResetDefaults:
		ID = "IronResetDefaults"
		isNative = True
		class IronResetDefaults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronResetPartAlignment:
		ID = "IronResetPartAlignment"
		isNative = True
		class IronResetPartAlignment_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ScanSurface:
		ID = "ScanSurface"
		isNative = True
		class ScanSurface_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSetupSheet:
		ID = "IronSetupSheet"
		isNative = True
		class IronSetupSheet_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSetupSheetConfigurations:
		ID = "IronSetupSheetConfigurations"
		isNative = True
		class IronSetupSheetConfigurations_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSetupSheetSwitchboard:
		ID = "IronSetupSheetSwitchboard"
		isNative = True
		class IronSetupSheetSwitchboard_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronShowHideTool:
		ID = "IronShowHideTool"
		isNative = True
		class IronShowHideTool_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class IronShowHideToolOnToolpath:
		ID = "IronShowHideToolOnToolpath"
		isNative = True
	class IronShowHideToolHolder:
		ID = "IronShowHideToolHolder"
		isNative = True
	class IronShowHideToolShaft:
		ID = "IronShowHideToolShaft"
		isNative = True
	class IronShowHideToolOnCursor:
		ID = "IronShowHideToolOnCursor"
		isNative = True
	class IronShowHideToolpathMoves:
		ID = "IronShowHideToolpathMoves"
		isNative = True
		class IronShowHideToolpathMoves_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class IronShowHideToolpathMovesLinks:
		ID = "IronShowHideToolpathMovesLinks"
		isNative = True
	class IronShowHideToolpathMovesLeads:
		ID = "IronShowHideToolpathMovesLeads"
		isNative = True
	class IronShowHideToolpathMovesCutting:
		ID = "IronShowHideToolpathMovesCutting"
		isNative = True
	class IronShowHideToolpathPoints:
		ID = "IronShowHideToolpathPoints"
		isNative = True
	class IronShowHideToolpathAxes:
		ID = "IronShowHideToolpathAxes"
		isNative = True
	class IronShowLog:
		ID = "IronShowLog"
		isNative = True
		class IronShowLog_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowNestLog:
		ID = "ShowNestLog"
		isNative = True
		class ShowNestLog_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPartAlignmentInfo:
		ID = "IronPartAlignmentInfo"
		isNative = True
		class IronPartAlignmentInfo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronShowResults:
		ID = "IronShowResults"
		isNative = True
		class IronShowResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStoreAsTemplate:
		ID = "IronStoreAsTemplate"
		isNative = True
		class IronStoreAsTemplate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStoreAsHoleTemplate:
		ID = "IronStoreAsHoleTemplate"
		isNative = True
		class IronStoreAsHoleTemplate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSuppress:
		ID = "IronSuppress"
		isNative = True
		class IronSuppress_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class IronSyncActiveSetup:
		ID = "IronSyncActiveSetup"
		isNative = True
		class IronSyncActiveSetup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class IronSyncOrientationActiveSetup:
		ID = "IronSyncOrientationActiveSetup"
		isNative = True
	class IronSyncVisibilityActiveSetup:
		ID = "IronSyncVisibilityActiveSetup"
		isNative = True
	class IronTaskManager:
		ID = "IronTaskManager"
		isNative = True
		class IronTaskManager_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronTemplateLibrary:
		ID = "IronTemplateLibrary"
		isNative = True
		class IronTemplateLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMTemplateLibraryDeleteLocalTestingAssetsCommand:
		ID = "CAMTemplateLibraryDeleteLocalTestingAssetsCommand"
		isNative = True
		class CAMTemplateLibraryDeleteLocalTestingAssetsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMTemplateLibraryImportTemplateCommand:
		ID = "CAMTemplateLibraryImportTemplateCommand"
		isNative = True
		class CAMTemplateLibraryImportTemplateCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolLibrary:
		ID = "IronToolLibrary"
		isNative = True
		class IronToolLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathPreview:
		ID = "IronToolpathPreview"
		isNative = True
		class IronToolpathPreview_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathVisibilityToggle:
		ID = "IronToolpathVisibilityToggle"
		isNative = True
		class IronToolpathVisibilityToggle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronTranslation:
		ID = "IronTranslation"
		isNative = True
		class IronTranslation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronUndrawAllToolpathOps:
		ID = "IronUndrawAllToolpathOps"
		isNative = True
		class IronUndrawAllToolpathOps_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronUndrawAllToolpathsInParent:
		ID = "IronUndrawAllToolpathsInParent"
		isNative = True
		class IronUndrawAllToolpathsInParent_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronUnisolateAllCmd:
		ID = "IronUnisolateAllCmd"
		isNative = True
		class IronUnisolateAllCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronUnisolateCmd:
		ID = "IronUnisolateCmd"
		isNative = True
		class IronUnisolateCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewNcCode:
		ID = "IronViewNcCode"
		isNative = True
		class IronViewNcCode_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientation:
		ID = "IronViewOrientation"
		isNative = True
		class IronViewOrientation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationTop:
		ID = "IronViewOrientationTop"
		isNative = True
		class IronViewOrientationTop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationBottom:
		ID = "IronViewOrientationBottom"
		isNative = True
		class IronViewOrientationBottom_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationFront:
		ID = "IronViewOrientationFront"
		isNative = True
		class IronViewOrientationFront_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationBack:
		ID = "IronViewOrientationBack"
		isNative = True
		class IronViewOrientationBack_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationLeft:
		ID = "IronViewOrientationLeft"
		isNative = True
		class IronViewOrientationLeft_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationRight:
		ID = "IronViewOrientationRight"
		isNative = True
		class IronViewOrientationRight_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewOrientationIso:
		ID = "IronViewOrientationIso"
		isNative = True
		class IronViewOrientationIso_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronViewStock:
		ID = "IronViewStock"
		isNative = True
		class IronViewStock_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxListControlDefinition"
	class IronTransparentStock:
		ID = "IronTransparentStock"
		isNative = True
	class IronInProcessStockDisplay:
		ID = "IronInProcessStockDisplay"
		isNative = True
	class IronViewToolpath:
		ID = "IronViewToolpath"
		isNative = True
		class IronViewToolpath_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class BrowserVisibilityBulb:
		ID = "BrowserVisibilityBulb"
		isNative = True
		class BrowserVisibilityBulb_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class CAMMoveComponentsCommand:
		ID = "CAMMoveComponentsCommand"
		isNative = True
		class CAMMoveComponentsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CollisionDetectionCmd:
		ID = "CollisionDetectionCmd"
		isNative = True
		class CollisionDetectionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMinimizeBoundingBox:
		ID = "IronMinimizeBoundingBox"
		isNative = True
		class IronMinimizeBoundingBox_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveViewOrientationResults:
		ID = "IronAdditiveViewOrientationResults"
		isNative = True
		class IronAdditiveViewOrientationResults_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPlaceOnPlatform:
		ID = "IronPlaceOnPlatform"
		isNative = True
		class IronPlaceOnPlatform_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDeleteNonIronObject:
		ID = "IronDeleteNonIronObject"
		isNative = True
		class IronDeleteNonIronObject_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSimulation:
		ID = "IronSimulation"
		isNative = True
		class IronSimulation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCreateSetupsFromWorkingModel:
		ID = "IronCreateSetupsFromWorkingModel"
		isNative = True
		class IronCreateSetupsFromWorkingModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronCreateSetupFromWorkingModel:
		ID = "IronCreateSetupFromWorkingModel"
		isNative = True
		class IronCreateSetupFromWorkingModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToggleBendLineVisibility:
		ID = "IronToggleBendLineVisibility"
		isNative = True
		class IronToggleBendLineVisibility_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronUpdateWorkingModels:
		ID = "IronUpdateWorkingModels"
		isNative = True
		class IronUpdateWorkingModels_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ActivateWorkingModel:
		ID = "ActivateWorkingModel"
		isNative = True
		class ActivateWorkingModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NeuCAMImportCommand:
		ID = "NeuCAMImportCommand"
		isNative = True
		class NeuCAMImportCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronSetup:
		ID = "IronSetup"
		isNative = True
		class IronSetup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronPattern:
		ID = "IronPattern"
		isNative = True
		class IronPattern_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAddToNewPattern:
		ID = "IronAddToNewPattern"
		isNative = True
		class IronAddToNewPattern_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditOperation:
		ID = "IronEditOperation"
		isNative = True
		class IronEditOperation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStock:
		ID = "IronStock"
		isNative = True
		class IronStock_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathTrim:
		ID = "IronToolpathTrim"
		isNative = True
		class IronToolpathTrim_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathEditDelete:
		ID = "IronToolpathEditDelete"
		isNative = True
		class IronToolpathEditDelete_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathEditLeadsLinks:
		ID = "IronToolpathEditLeadsLinks"
		isNative = True
		class IronToolpathEditLeadsLinks_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathEditToolChange:
		ID = "IronToolpathEditToolChange"
		isNative = True
		class IronToolpathEditToolChange_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditBuildStrategyOperation:
		ID = "IronEditBuildStrategyOperation"
		isNative = True
		class IronEditBuildStrategyOperation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronEditAdditiveProcessSimulation:
		ID = "IronEditAdditiveProcessSimulation"
		isNative = True
		class IronEditAdditiveProcessSimulation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronToolpathEditMoveStartPoints:
		ID = "IronToolpathEditMoveStartPoints"
		isNative = True
		class IronToolpathEditMoveStartPoints_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronNewOperation:
		ID = "IronNewOperation"
		isNative = True
		class IronNewOperation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronNewSelection:
		ID = "IronNewSelection"
		isNative = True
		class IronNewSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronNewToolpathEdit:
		ID = "IronNewToolpathEdit"
		isNative = True
		class IronNewToolpathEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveSupport:
		ID = "IronAdditiveSupport"
		isNative = True
		class IronAdditiveSupport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditiveOrientations:
		ID = "IronAdditiveOrientations"
		isNative = True
		class IronAdditiveOrientations_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDerivedOperation:
		ID = "IronDerivedOperation"
		isNative = True
		class IronDerivedOperation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Iron2DMilling:
		ID = "Iron2DMilling"
		isNative = True
		class Iron2DMilling_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_featureRecognition:
		ID = "IronStrategy_featureRecognition"
		isNative = True
		class IronStrategy_featureRecognition_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_contourFeatureFolder:
		ID = "IronStrategy_contourFeatureFolder"
		isNative = True
		class IronStrategy_contourFeatureFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_holeFeatureFolder:
		ID = "IronStrategy_holeFeatureFolder"
		isNative = True
		class IronStrategy_holeFeatureFolder_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_adaptive2d:
		ID = "IronStrategy_adaptive2d"
		isNative = True
		class IronStrategy_adaptive2d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pocket2d:
		ID = "IronStrategy_pocket2d"
		isNative = True
		class IronStrategy_pocket2d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_contour2d:
		ID = "IronStrategy_contour2d"
		isNative = True
		class IronStrategy_contour2d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_face:
		ID = "IronStrategy_face"
		isNative = True
		class IronStrategy_face_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_slot:
		ID = "IronStrategy_slot"
		isNative = True
		class IronStrategy_slot_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_path3d:
		ID = "IronStrategy_path3d"
		isNative = True
		class IronStrategy_path3d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_thread:
		ID = "IronStrategy_thread"
		isNative = True
		class IronStrategy_thread_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_circular:
		ID = "IronStrategy_circular"
		isNative = True
		class IronStrategy_circular_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_bore:
		ID = "IronStrategy_bore"
		isNative = True
		class IronStrategy_bore_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_engrave:
		ID = "IronStrategy_engrave"
		isNative = True
		class IronStrategy_engrave_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_chamfer2d:
		ID = "IronStrategy_chamfer2d"
		isNative = True
		class IronStrategy_chamfer2d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_probe:
		ID = "IronStrategy_probe"
		isNative = True
		class IronStrategy_probe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_geometry_contours:
		ID = "IronStrategy_geometry_contours"
		isNative = True
		class IronStrategy_geometry_contours_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_geometry_pockets:
		ID = "IronStrategy_geometry_pockets"
		isNative = True
		class IronStrategy_geometry_pockets_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_geometry_silhouette:
		ID = "IronStrategy_geometry_silhouette"
		isNative = True
		class IronStrategy_geometry_silhouette_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pocket_recognition:
		ID = "IronStrategy_pocket_recognition"
		isNative = True
		class IronStrategy_pocket_recognition_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Iron2DMilling_derived:
		ID = "Iron2DMilling_derived"
		isNative = True
		class Iron2DMilling_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_adaptive2d_derived:
		ID = "IronStrategy_adaptive2d_derived"
		isNative = True
		class IronStrategy_adaptive2d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pocket2d_derived:
		ID = "IronStrategy_pocket2d_derived"
		isNative = True
		class IronStrategy_pocket2d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_contour2d_derived:
		ID = "IronStrategy_contour2d_derived"
		isNative = True
		class IronStrategy_contour2d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_face_derived:
		ID = "IronStrategy_face_derived"
		isNative = True
		class IronStrategy_face_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_slot_derived:
		ID = "IronStrategy_slot_derived"
		isNative = True
		class IronStrategy_slot_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_path3d_derived:
		ID = "IronStrategy_path3d_derived"
		isNative = True
		class IronStrategy_path3d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_thread_derived:
		ID = "IronStrategy_thread_derived"
		isNative = True
		class IronStrategy_thread_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_circular_derived:
		ID = "IronStrategy_circular_derived"
		isNative = True
		class IronStrategy_circular_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_bore_derived:
		ID = "IronStrategy_bore_derived"
		isNative = True
		class IronStrategy_bore_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_engrave_derived:
		ID = "IronStrategy_engrave_derived"
		isNative = True
		class IronStrategy_engrave_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_chamfer2d_derived:
		ID = "IronStrategy_chamfer2d_derived"
		isNative = True
		class IronStrategy_chamfer2d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_probe_derived:
		ID = "IronStrategy_probe_derived"
		isNative = True
		class IronStrategy_probe_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDrilling:
		ID = "IronDrilling"
		isNative = True
		class IronDrilling_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_drill:
		ID = "IronStrategy_drill"
		isNative = True
		class IronStrategy_drill_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDrilling_derived:
		ID = "IronDrilling_derived"
		isNative = True
		class IronDrilling_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_drill_derived:
		ID = "IronStrategy_drill_derived"
		isNative = True
		class IronStrategy_drill_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Iron3DMilling:
		ID = "Iron3DMilling"
		isNative = True
		class Iron3DMilling_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_adaptive:
		ID = "IronStrategy_adaptive"
		isNative = True
		class IronStrategy_adaptive_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pocket_new:
		ID = "IronStrategy_pocket_new"
		isNative = True
		class IronStrategy_pocket_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_horizontal_new:
		ID = "IronStrategy_horizontal_new"
		isNative = True
		class IronStrategy_horizontal_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_contour_new:
		ID = "IronStrategy_contour_new"
		isNative = True
		class IronStrategy_contour_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_ramp:
		ID = "IronStrategy_ramp"
		isNative = True
		class IronStrategy_ramp_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_parallel_new:
		ID = "IronStrategy_parallel_new"
		isNative = True
		class IronStrategy_parallel_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_scallop_new:
		ID = "IronStrategy_scallop_new"
		isNative = True
		class IronStrategy_scallop_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pencil_new:
		ID = "IronStrategy_pencil_new"
		isNative = True
		class IronStrategy_pencil_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_radial_new:
		ID = "IronStrategy_radial_new"
		isNative = True
		class IronStrategy_radial_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_spiral_new:
		ID = "IronStrategy_spiral_new"
		isNative = True
		class IronStrategy_spiral_new_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_morphed_spiral:
		ID = "IronStrategy_morphed_spiral"
		isNative = True
		class IronStrategy_morphed_spiral_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_project:
		ID = "IronStrategy_project"
		isNative = True
		class IronStrategy_project_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_blend:
		ID = "IronStrategy_blend"
		isNative = True
		class IronStrategy_blend_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_morph:
		ID = "IronStrategy_morph"
		isNative = True
		class IronStrategy_morph_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_steep_and_shallow:
		ID = "IronStrategy_steep_and_shallow"
		isNative = True
		class IronStrategy_steep_and_shallow_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_flat:
		ID = "IronStrategy_flat"
		isNative = True
		class IronStrategy_flat_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_rest_finishing:
		ID = "IronStrategy_rest_finishing"
		isNative = True
		class IronStrategy_rest_finishing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_flow:
		ID = "IronStrategy_flow"
		isNative = True
		class IronStrategy_flow_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Iron3DMilling_derived:
		ID = "Iron3DMilling_derived"
		isNative = True
		class Iron3DMilling_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_adaptive_derived:
		ID = "IronStrategy_adaptive_derived"
		isNative = True
		class IronStrategy_adaptive_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pocket_new_derived:
		ID = "IronStrategy_pocket_new_derived"
		isNative = True
		class IronStrategy_pocket_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_horizontal_new_derived:
		ID = "IronStrategy_horizontal_new_derived"
		isNative = True
		class IronStrategy_horizontal_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_contour_new_derived:
		ID = "IronStrategy_contour_new_derived"
		isNative = True
		class IronStrategy_contour_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_ramp_derived:
		ID = "IronStrategy_ramp_derived"
		isNative = True
		class IronStrategy_ramp_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_parallel_new_derived:
		ID = "IronStrategy_parallel_new_derived"
		isNative = True
		class IronStrategy_parallel_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_scallop_new_derived:
		ID = "IronStrategy_scallop_new_derived"
		isNative = True
		class IronStrategy_scallop_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_pencil_new_derived:
		ID = "IronStrategy_pencil_new_derived"
		isNative = True
		class IronStrategy_pencil_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_radial_new_derived:
		ID = "IronStrategy_radial_new_derived"
		isNative = True
		class IronStrategy_radial_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_spiral_new_derived:
		ID = "IronStrategy_spiral_new_derived"
		isNative = True
		class IronStrategy_spiral_new_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_morphed_spiral_derived:
		ID = "IronStrategy_morphed_spiral_derived"
		isNative = True
		class IronStrategy_morphed_spiral_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_project_derived:
		ID = "IronStrategy_project_derived"
		isNative = True
		class IronStrategy_project_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_blend_derived:
		ID = "IronStrategy_blend_derived"
		isNative = True
		class IronStrategy_blend_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_morph_derived:
		ID = "IronStrategy_morph_derived"
		isNative = True
		class IronStrategy_morph_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_steep_and_shallow_derived:
		ID = "IronStrategy_steep_and_shallow_derived"
		isNative = True
		class IronStrategy_steep_and_shallow_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_flat_derived:
		ID = "IronStrategy_flat_derived"
		isNative = True
		class IronStrategy_flat_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_rest_finishing_derived:
		ID = "IronStrategy_rest_finishing_derived"
		isNative = True
		class IronStrategy_rest_finishing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_flow_derived:
		ID = "IronStrategy_flow_derived"
		isNative = True
		class IronStrategy_flow_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_manual:
		ID = "IronStrategy_manual"
		isNative = True
		class IronStrategy_manual_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMultiAxisMilling:
		ID = "IronMultiAxisMilling"
		isNative = True
		class IronMultiAxisMilling_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_swarf5d:
		ID = "IronStrategy_swarf5d"
		isNative = True
		class IronStrategy_swarf5d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_multiAxisContour:
		ID = "IronStrategy_multiAxisContour"
		isNative = True
		class IronStrategy_multiAxisContour_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_rotary_finishing:
		ID = "IronStrategy_rotary_finishing"
		isNative = True
		class IronStrategy_rotary_finishing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronMultiAxisMilling_derived:
		ID = "IronMultiAxisMilling_derived"
		isNative = True
		class IronMultiAxisMilling_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_swarf5d_derived:
		ID = "IronStrategy_swarf5d_derived"
		isNative = True
		class IronStrategy_swarf5d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_multiAxisContour_derived:
		ID = "IronStrategy_multiAxisContour_derived"
		isNative = True
		class IronStrategy_multiAxisContour_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_rotary_finishing_derived:
		ID = "IronStrategy_rotary_finishing_derived"
		isNative = True
		class IronStrategy_rotary_finishing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronTurning:
		ID = "IronTurning"
		isNative = True
		class IronTurning_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileRoughing:
		ID = "IronStrategy_turningProfileRoughing"
		isNative = True
		class IronStrategy_turningProfileRoughing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileFinishing:
		ID = "IronStrategy_turningProfileFinishing"
		isNative = True
		class IronStrategy_turningProfileFinishing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningRoughing:
		ID = "IronStrategy_turningRoughing"
		isNative = True
		class IronStrategy_turningRoughing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileGroove:
		ID = "IronStrategy_turningProfileGroove"
		isNative = True
		class IronStrategy_turningProfileGroove_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningAdaptiveRoughing:
		ID = "IronStrategy_turningAdaptiveRoughing"
		isNative = True
		class IronStrategy_turningAdaptiveRoughing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningFace:
		ID = "IronStrategy_turningFace"
		isNative = True
		class IronStrategy_turningFace_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningGroove:
		ID = "IronStrategy_turningGroove"
		isNative = True
		class IronStrategy_turningGroove_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningChamfer:
		ID = "IronStrategy_turningChamfer"
		isNative = True
		class IronStrategy_turningChamfer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningPart:
		ID = "IronStrategy_turningPart"
		isNative = True
		class IronStrategy_turningPart_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningThread:
		ID = "IronStrategy_turningThread"
		isNative = True
		class IronStrategy_turningThread_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningStockTransfer:
		ID = "IronStrategy_turningStockTransfer"
		isNative = True
		class IronStrategy_turningStockTransfer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindleGrab:
		ID = "IronStrategy_turningSecondarySpindleGrab"
		isNative = True
		class IronStrategy_turningSecondarySpindleGrab_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindlePull:
		ID = "IronStrategy_turningSecondarySpindlePull"
		isNative = True
		class IronStrategy_turningSecondarySpindlePull_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindleReturn:
		ID = "IronStrategy_turningSecondarySpindleReturn"
		isNative = True
		class IronStrategy_turningSecondarySpindleReturn_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronTurning_derived:
		ID = "IronTurning_derived"
		isNative = True
		class IronTurning_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileRoughing_derived:
		ID = "IronStrategy_turningProfileRoughing_derived"
		isNative = True
		class IronStrategy_turningProfileRoughing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileFinishing_derived:
		ID = "IronStrategy_turningProfileFinishing_derived"
		isNative = True
		class IronStrategy_turningProfileFinishing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningRoughing_derived:
		ID = "IronStrategy_turningRoughing_derived"
		isNative = True
		class IronStrategy_turningRoughing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningProfileGroove_derived:
		ID = "IronStrategy_turningProfileGroove_derived"
		isNative = True
		class IronStrategy_turningProfileGroove_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningAdaptiveRoughing_derived:
		ID = "IronStrategy_turningAdaptiveRoughing_derived"
		isNative = True
		class IronStrategy_turningAdaptiveRoughing_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningFace_derived:
		ID = "IronStrategy_turningFace_derived"
		isNative = True
		class IronStrategy_turningFace_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningGroove_derived:
		ID = "IronStrategy_turningGroove_derived"
		isNative = True
		class IronStrategy_turningGroove_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningChamfer_derived:
		ID = "IronStrategy_turningChamfer_derived"
		isNative = True
		class IronStrategy_turningChamfer_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningPart_derived:
		ID = "IronStrategy_turningPart_derived"
		isNative = True
		class IronStrategy_turningPart_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningThread_derived:
		ID = "IronStrategy_turningThread_derived"
		isNative = True
		class IronStrategy_turningThread_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningStockTransfer_derived:
		ID = "IronStrategy_turningStockTransfer_derived"
		isNative = True
		class IronStrategy_turningStockTransfer_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindleGrab_derived:
		ID = "IronStrategy_turningSecondarySpindleGrab_derived"
		isNative = True
		class IronStrategy_turningSecondarySpindleGrab_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindlePull_derived:
		ID = "IronStrategy_turningSecondarySpindlePull_derived"
		isNative = True
		class IronStrategy_turningSecondarySpindlePull_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_turningSecondarySpindleReturn_derived:
		ID = "IronStrategy_turningSecondarySpindleReturn_derived"
		isNative = True
		class IronStrategy_turningSecondarySpindleReturn_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronWLPC:
		ID = "IronWLPC"
		isNative = True
		class IronWLPC_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_jet2d:
		ID = "IronStrategy_jet2d"
		isNative = True
		class IronStrategy_jet2d_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronWLPC_derived:
		ID = "IronWLPC_derived"
		isNative = True
		class IronWLPC_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_jet2d_derived:
		ID = "IronStrategy_jet2d_derived"
		isNative = True
		class IronStrategy_jet2d_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_create_form_mill:
		ID = "IronStrategy_create_form_mill"
		isNative = True
		class IronStrategy_create_form_mill_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronProbing:
		ID = "IronProbing"
		isNative = True
		class IronProbing_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_inspectSurface:
		ID = "IronStrategy_inspectSurface"
		isNative = True
		class IronStrategy_inspectSurface_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_probe_geometry:
		ID = "IronStrategy_probe_geometry"
		isNative = True
		class IronStrategy_probe_geometry_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_part_alignment:
		ID = "IronStrategy_part_alignment"
		isNative = True
		class IronStrategy_part_alignment_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_datum:
		ID = "IronStrategy_datum"
		isNative = True
		class IronStrategy_datum_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_manual_inspect:
		ID = "IronStrategy_manual_inspect"
		isNative = True
		class IronStrategy_manual_inspect_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_cmm_inspection_setup:
		ID = "IronStrategy_cmm_inspection_setup"
		isNative = True
		class IronStrategy_cmm_inspection_setup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronAdditive:
		ID = "IronAdditive"
		isNative = True
		class IronAdditive_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_additive_optimize_orientation:
		ID = "IronStrategy_additive_optimize_orientation"
		isNative = True
		class IronStrategy_additive_optimize_orientation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_areavolume_additive_support:
		ID = "IronStrategy_areavolume_additive_support"
		isNative = True
		class IronStrategy_areavolume_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_areabar_additive_support:
		ID = "IronStrategy_areabar_additive_support"
		isNative = True
		class IronStrategy_areabar_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_areapolyline_additive_support:
		ID = "IronStrategy_areapolyline_additive_support"
		isNative = True
		class IronStrategy_areapolyline_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_skeletonpolyline_additive_support:
		ID = "IronStrategy_skeletonpolyline_additive_support"
		isNative = True
		class IronStrategy_skeletonpolyline_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_lattice_additive_support:
		ID = "IronStrategy_lattice_additive_support"
		isNative = True
		class IronStrategy_lattice_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_downoriented_additive_support:
		ID = "IronStrategy_downoriented_additive_support"
		isNative = True
		class IronStrategy_downoriented_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_edgepolyline_additive_support:
		ID = "IronStrategy_edgepolyline_additive_support"
		isNative = True
		class IronStrategy_edgepolyline_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_clustercontourpolyline_additive_support:
		ID = "IronStrategy_clustercontourpolyline_additive_support"
		isNative = True
		class IronStrategy_clustercontourpolyline_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_surroundvolumepolyline_additive_support:
		ID = "IronStrategy_surroundvolumepolyline_additive_support"
		isNative = True
		class IronStrategy_surroundvolumepolyline_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_baseplate_additive_support:
		ID = "IronStrategy_baseplate_additive_support"
		isNative = True
		class IronStrategy_baseplate_additive_support_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_additive_buildstyle:
		ID = "IronStrategy_additive_buildstyle"
		isNative = True
		class IronStrategy_additive_buildstyle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_additive_printtime:
		ID = "IronStrategy_additive_printtime"
		isNative = True
		class IronStrategy_additive_printtime_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_additive_individual_strategies:
		ID = "IronStrategy_additive_individual_strategies"
		isNative = True
		class IronStrategy_additive_individual_strategies_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDED:
		ID = "IronDED"
		isNative = True
		class IronDED_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_feature_construction:
		ID = "IronStrategy_feature_construction"
		isNative = True
		class IronStrategy_feature_construction_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronDED_derived:
		ID = "IronDED_derived"
		isNative = True
		class IronDED_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class IronStrategy_feature_construction_derived:
		ID = "IronStrategy_feature_construction_derived"
		isNative = True
		class IronStrategy_feature_construction_derived_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NeuCAMExportXMLCommand:
		ID = "NeuCAMExportXMLCommand"
		isNative = True
		class NeuCAMExportXMLCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMCreateLibrariesCommand:
		ID = "CAMCreateLibrariesCommand"
		isNative = True
		class CAMCreateLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMCreateToolsCommand:
		ID = "CAMCreateToolsCommand"
		isNative = True
		class CAMCreateToolsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMDeleteLibrariesCommand:
		ID = "CAMDeleteLibrariesCommand"
		isNative = True
		class CAMDeleteLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMDeleteToolsCommand:
		ID = "CAMDeleteToolsCommand"
		isNative = True
		class CAMDeleteToolsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMDuplicateLibrariesCommand:
		ID = "CAMDuplicateLibrariesCommand"
		isNative = True
		class CAMDuplicateLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMEditLibrariesCommand:
		ID = "CAMEditLibrariesCommand"
		isNative = True
		class CAMEditLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMEditToolsCmdCommand:
		ID = "CAMEditToolsCmdCommand"
		isNative = True
		class CAMEditToolsCmdCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMExportLibrariesCommand:
		ID = "CAMExportLibrariesCommand"
		isNative = True
		class CAMExportLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMImportLibrariesCommand:
		ID = "CAMImportLibrariesCommand"
		isNative = True
		class CAMImportLibrariesCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMSetToolGuidCommand:
		ID = "CAMSetToolGuidCommand"
		isNative = True
		class CAMSetToolGuidCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMPresetToolLibraryActionsCommand:
		ID = "CAMPresetToolLibraryActionsCommand"
		isNative = True
		class CAMPresetToolLibraryActionsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMClearToolLibraryActionsCommand:
		ID = "CAMClearToolLibraryActionsCommand"
		isNative = True
		class CAMClearToolLibraryActionsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMSetMachineCommand:
		ID = "CAMSetMachineCommand"
		isNative = True
		class CAMSetMachineCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMSetPostScriptCommand:
		ID = "CAMSetPostScriptCommand"
		isNative = True
		class CAMSetPostScriptCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMTestSimulationPlayerCmd:
		ID = "CAMTestSimulationPlayerCmd"
		isNative = True
		class CAMTestSimulationPlayerCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderArmPreview:
		ID = "MachineBuilder::ArmPreview"
		isNative = True
		class MachineBuilderArmPreview_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderMoveComponents:
		ID = "MachineBuilder::MoveComponents"
		isNative = True
		class MachineBuilderMoveComponents_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderSaveAs:
		ID = "MachineBuilder::SaveAs"
		isNative = True
		class MachineBuilderSaveAs_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderStart:
		ID = "MachineBuilder::Start"
		isNative = True
		class MachineBuilderStart_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderStop:
		ID = "MachineBuilder::Stop"
		isNative = True
		class MachineBuilderStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderMachineEdit:
		ID = "MachineBuilder::MachineEdit"
		isNative = True
		class MachineBuilderMachineEdit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderPreview:
		ID = "MachineBuilder::Preview"
		isNative = True
		class MachineBuilderPreview_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderMachineSelection:
		ID = "MachineBuilder::MachineSelection"
		isNative = True
		class MachineBuilderMachineSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MachineBuilderModelSelection:
		ID = "MachineBuilder::ModelSelection"
		isNative = True
		class MachineBuilderModelSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NewElectronDesignMenuCommand:
		ID = "NewElectronDesignMenuCommand"
		isNative = True
		class NewElectronDesignMenuCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewElectronPcbDocumentCommand:
		ID = "NewElectronPcbDocumentCommand"
		isNative = True
		class NewElectronPcbDocumentCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NewElectronSchDocumentCommand:
		ID = "NewElectronSchDocumentCommand"
		isNative = True
		class NewElectronSchDocumentCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class NewElectronLbrDocumentCommand:
		ID = "NewElectronLbrDocumentCommand"
		isNative = True
		class NewElectronLbrDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ElectronPcb3DView:
		ID = "Electron::Pcb3DView"
		isNative = True
		class ElectronPcb3DView_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPcb3DViewAdvanced:
		ID = "Electron::Pcb3DViewAdvanced"
		isNative = True
		class ElectronPcb3DViewAdvanced_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBExportBrdCmd:
		ID = "PCBExportBrdCmd"
		isNative = True
		class PCBExportBrdCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PCBLinkToBrdCmd:
		ID = "PCBLinkToBrdCmd"
		isNative = True
		class PCBLinkToBrdCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Package3DCmd:
		ID = "Package3DCmd"
		isNative = True
		class Package3DCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class Package3DStop:
		ID = "Package3DStop"
		isNative = True
		class Package3DStop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class Package3DCreateCmd:
		ID = "Package3DCreateCmd"
		isNative = True
		class Package3DCreateCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RemovePCB3DLinkCmd:
		ID = "RemovePCB3DLinkCmd"
		isNative = True
		class RemovePCB3DLinkCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class FootprintSketchCreateCmd:
		ID = "FootprintSketchCreateCmd"
		isNative = True
		class FootprintSketchCreateCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NewElectronDesignDocumentCommand:
		ID = "NewElectronDesignDocumentCommand"
		isNative = True
		class NewElectronDesignDocumentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SwitchPcbDocCmd:
		ID = "SwitchPcbDocCmd"
		isNative = True
		class SwitchPcbDocCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SwitchSchDocCmd:
		ID = "SwitchSchDocCmd"
		isNative = True
		class SwitchSchDocCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GetLatestElectronCmd:
		ID = "GetLatestElectronCmd"
		isNative = True
		class GetLatestElectronCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GetLatestPcbCmd:
		ID = "GetLatestPcbCmd"
		isNative = True
		class GetLatestPcbCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class GetLatestSchCmd:
		ID = "GetLatestSchCmd"
		isNative = True
		class GetLatestSchCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LaunchUndoCmdDef:
		ID = "LaunchUndoCmdDef"
		isNative = True
		class LaunchUndoCmdDef_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class LaunchRedoCmdDef:
		ID = "LaunchRedoCmdDef"
		isNative = True
		class LaunchRedoCmdDef_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReferenceToPCBCmd:
		ID = "ReferenceToPCBCmd"
		isNative = True
		class ReferenceToPCBCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ReferenceToSCHCmd:
		ID = "ReferenceToSCHCmd"
		isNative = True
		class ReferenceToSCHCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RemovePCBLinkCmd:
		ID = "RemovePCBLinkCmd"
		isNative = True
		class RemovePCBLinkCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class RemoveSCHLinkCmd:
		ID = "RemoveSCHLinkCmd"
		isNative = True
		class RemoveSCHLinkCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSaveAllCmd:
		ID = "ElectronSaveAllCmd"
		isNative = True
		class ElectronSaveAllCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ElectronSaveAsAllCmd:
		ID = "ElectronSaveAsAllCmd"
		isNative = True
		class ElectronSaveAsAllCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class SaveBOMDataCmd:
		ID = "SaveBOMDataCmd"
		isNative = True
		class SaveBOMDataCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class AnsysCmd:
		ID = "AnsysCmd"
		isNative = True
		class AnsysCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CAMOdbExportCmd:
		ID = "CAMOdbExportCmd"
		isNative = True
		class CAMOdbExportCmd_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditorSidePanelOpenCommand:
		ID = "EditorSidePanelOpenCommand"
		isNative = True
		class EditorSidePanelOpenCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class EditorSidePanelCloseCommand:
		ID = "EditorSidePanelCloseCommand"
		isNative = True
		class EditorSidePanelCloseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowElectronDescriptionCommand:
		ID = "ShowElectronDescriptionCommand"
		isNative = True
		class ShowElectronDescriptionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideElectronDescriptionCommand:
		ID = "HideElectronDescriptionCommand"
		isNative = True
		class HideElectronDescriptionCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ContentManagerPanelOpenCommand:
		ID = "ContentManagerPanelOpenCommand"
		isNative = True
		class ContentManagerPanelOpenCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ContentManagerPanelCloseCommand:
		ID = "ContentManagerPanelCloseCommand"
		isNative = True
		class ContentManagerPanelCloseCommand_control:
			isVisible = True
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowElectronDesignManagerCommand:
		ID = "ShowElectronDesignManagerCommand"
		isNative = True
		class ShowElectronDesignManagerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideElectronDesignManagerCommand:
		ID = "HideElectronDesignManagerCommand"
		isNative = True
		class HideElectronDesignManagerCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowElectronInspectorCommand:
		ID = "ShowElectronInspectorCommand"
		isNative = True
		class ShowElectronInspectorCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideElectronInspectorCommand:
		ID = "HideElectronInspectorCommand"
		isNative = True
		class HideElectronInspectorCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowCommandGuidanceCommand:
		ID = "ShowCommandGuidanceCommand"
		isNative = True
		class ShowCommandGuidanceCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideCommandGuidanceCommand:
		ID = "HideCommandGuidanceCommand"
		isNative = True
		class HideCommandGuidanceCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowElectronSelectionFilterCommand:
		ID = "ShowElectronSelectionFilterCommand"
		isNative = True
		class ShowElectronSelectionFilterCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideElectronSelectionFilterCommand:
		ID = "HideElectronSelectionFilterCommand"
		isNative = True
		class HideElectronSelectionFilterCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ShowElectronSheetsCommand:
		ID = "ShowElectronSheetsCommand"
		isNative = True
		class ShowElectronSheetsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class HideElectronSheetsCommand:
		ID = "HideElectronSheetsCommand"
		isNative = True
		class HideElectronSheetsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class UpdateEagleLibrariesVersions:
		ID = "UpdateEagleLibrariesVersions"
		isNative = True
		class UpdateEagleLibrariesVersions_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class RefreshEagleWIPLibraryCmd:
		ID = "RefreshEagleWIPLibraryCmd"
		isNative = True
		class RefreshEagleWIPLibraryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DeleteEagleWIPLibraryCmd:
		ID = "DeleteEagleWIPLibraryCmd"
		isNative = True
		class DeleteEagleWIPLibraryCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ElectronFocusEagleCommandLine:
		ID = "Electron::FocusEagleCommandLine"
		isNative = True
		class ElectronFocusEagleCommandLine_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class TogglePushViasCmd:
		ID = "TogglePushViasCmd"
		isNative = True
		class TogglePushViasCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class ViolationModeCommand:
		ID = "ViolationModeCommand"
		isNative = True
		class ViolationModeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "StandardListControlDefinition"
	class IgnoreViolatorsCommand:
		ID = "IgnoreViolatorsCommand"
		isNative = True
		class IgnoreViolatorsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PushViolatorsCommand:
		ID = "PushViolatorsCommand"
		isNative = True
		class PushViolatorsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class WalkaroundViolatorsCommand:
		ID = "WalkaroundViolatorsCommand"
		isNative = True
		class WalkaroundViolatorsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAddPart:
		ID = "Electron::AddPart"
		isNative = True
		class ElectronAddPart_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAddDesignBlock:
		ID = "Electron::AddDesignBlock"
		isNative = True
		class ElectronAddDesignBlock_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAlign:
		ID = "Electron::Align"
		isNative = True
		class ElectronAlign_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronArc:
		ID = "Electron::Arc"
		isNative = True
		class ElectronArc_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAttribute:
		ID = "Electron::Attribute"
		isNative = True
		class ElectronAttribute_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAutoRouter:
		ID = "Electron::AutoRouter"
		isNative = True
		class ElectronAutoRouter_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBoardShapeArc:
		ID = "Electron::BoardShapeArc"
		isNative = True
		class ElectronBoardShapeArc_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBoardShapeCircle:
		ID = "Electron::BoardShapeCircle"
		isNative = True
		class ElectronBoardShapeCircle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBoardShapePolyline:
		ID = "Electron::BoardShapePolyline"
		isNative = True
		class ElectronBoardShapePolyline_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBoardShapeSpline:
		ID = "Electron::BoardShapeSpline"
		isNative = True
		class ElectronBoardShapeSpline_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBom:
		ID = "Electron::Bom"
		isNative = True
		class ElectronBom_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronBus:
		ID = "Electron::Bus"
		isNative = True
		class ElectronBus_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCAMExport:
		ID = "Electron::CAMExport"
		isNative = True
		class ElectronCAMExport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCAMPreview:
		ID = "Electron::CAMPreview"
		isNative = True
		class ElectronCAMPreview_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCAMProcessor:
		ID = "Electron::CAMProcessor"
		isNative = True
		class ElectronCAMProcessor_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronChange:
		ID = "Electron::Change"
		isNative = True
		class ElectronChange_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCircle:
		ID = "Electron::Circle"
		isNative = True
		class ElectronCircle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronClass:
		ID = "Electron::Class"
		isNative = True
		class ElectronClass_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCopy:
		ID = "Electron::Copy"
		isNative = True
		class ElectronCopy_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCut:
		ID = "Electron::Cut"
		isNative = True
		class ElectronCut_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronDelete:
		ID = "Electron::Delete"
		isNative = True
		class ElectronDelete_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronDimension:
		ID = "Electron::Dimension"
		isNative = True
		class ElectronDimension_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronDisplay:
		ID = "Electron::Display"
		isNative = True
		class ElectronDisplay_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronDRC:
		ID = "Electron::DRC"
		isNative = True
		class ElectronDRC_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronERC:
		ID = "Electron::ERC"
		isNative = True
		class ElectronERC_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronErrors:
		ID = "Electron::Errors"
		isNative = True
		class ElectronErrors_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronFanout:
		ID = "Electron::Fanout"
		isNative = True
		class ElectronFanout_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronFlipBoard:
		ID = "Electron::FlipBoard"
		isNative = True
		class ElectronFlipBoard_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronGateSwap:
		ID = "Electron::GateSwap"
		isNative = True
		class ElectronGateSwap_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronGrid:
		ID = "Electron::Grid"
		isNative = True
		class ElectronGrid_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronGroup:
		ID = "Electron::Group"
		isNative = True
		class ElectronGroup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronGroupPolygon:
		ID = "Electron::GroupPolygon"
		isNative = True
		class ElectronGroupPolygon_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAddHole:
		ID = "Electron::AddHole"
		isNative = True
		class ElectronAddHole_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronInfo:
		ID = "Electron::Info"
		isNative = True
		class ElectronInfo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronInvoke:
		ID = "Electron::Invoke"
		isNative = True
		class ElectronInvoke_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronIpcNetlist:
		ID = "Electron::IpcNetlist"
		isNative = True
		class ElectronIpcNetlist_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronJunction:
		ID = "Electron::Junction"
		isNative = True
		class ElectronJunction_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLabel:
		ID = "Electron::Label"
		isNative = True
		class ElectronLabel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLayer:
		ID = "Electron::Layer"
		isNative = True
		class ElectronLayer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLine:
		ID = "Electron::Line"
		isNative = True
		class ElectronLine_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUnlinkLibrary:
		ID = "Electron::UnlinkLibrary"
		isNative = True
		class ElectronUnlinkLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLock:
		ID = "Electron::Lock"
		isNative = True
		class ElectronLock_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLockAll:
		ID = "Electron::LockAll"
		isNative = True
		class ElectronLockAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLockCurrentLayer:
		ID = "Electron::LockCurrentLayer"
		isNative = True
		class ElectronLockCurrentLayer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUnlockAll:
		ID = "Electron::UnlockAll"
		isNative = True
		class ElectronUnlockAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronCreateLibrary:
		ID = "Electron::CreateLibrary"
		isNative = True
		class ElectronCreateLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAddSimModel:
		ID = "Electron::AddSimModel"
		isNative = True
		class ElectronAddSimModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronMark:
		ID = "Electron::Mark"
		isNative = True
		class ElectronMark_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronMeander:
		ID = "Electron::Meander"
		isNative = True
		class ElectronMeander_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronMiter:
		ID = "Electron::Miter"
		isNative = True
		class ElectronMiter_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronMirror:
		ID = "Electron::Mirror"
		isNative = True
		class ElectronMirror_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronModule:
		ID = "Electron::Module"
		isNative = True
		class ElectronModule_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronMove:
		ID = "Electron::Move"
		isNative = True
		class ElectronMove_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronName:
		ID = "Electron::Name"
		isNative = True
		class ElectronName_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronNet:
		ID = "Electron::Net"
		isNative = True
		class ElectronNet_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronNewSymbol:
		ID = "Electron::NewSymbol"
		isNative = True
		class ElectronNewSymbol_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronNewPackage:
		ID = "Electron::NewPackage"
		isNative = True
		class ElectronNewPackage_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronNewDevice:
		ID = "Electron::NewDevice"
		isNative = True
		class ElectronNewDevice_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronOptimize:
		ID = "Electron::Optimize"
		isNative = True
		class ElectronOptimize_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPad:
		ID = "Electron::Pad"
		isNative = True
		class ElectronPad_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPadArray:
		ID = "Electron::PadArray"
		isNative = True
		class ElectronPadArray_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPaintRoller:
		ID = "Electron::PaintRoller"
		isNative = True
		class ElectronPaintRoller_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPaste:
		ID = "Electron::Paste"
		isNative = True
		class ElectronPaste_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPattern:
		ID = "Electron::Pattern"
		isNative = True
		class ElectronPattern_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPickAndPlace:
		ID = "Electron::PickAndPlace"
		isNative = True
		class ElectronPickAndPlace_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPin:
		ID = "Electron::Pin"
		isNative = True
		class ElectronPin_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPinArray:
		ID = "Electron::PinArray"
		isNative = True
		class ElectronPinArray_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPinSwap:
		ID = "Electron::PinSwap"
		isNative = True
		class ElectronPinSwap_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPShape:
		ID = "Electron::PShape"
		isNative = True
		class ElectronPShape_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPPour:
		ID = "Electron::PPour"
		isNative = True
		class ElectronPPour_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPCutout:
		ID = "Electron::PCutout"
		isNative = True
		class ElectronPCutout_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPolygon:
		ID = "Electron::Polygon"
		isNative = True
		class ElectronPolygon_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPolyHideFillAll:
		ID = "Electron::PolyHideFillAll"
		isNative = True
		class ElectronPolyHideFillAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPolyRefill:
		ID = "Electron::PolyRefill"
		isNative = True
		class ElectronPolyRefill_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPolygonizeCopy:
		ID = "Electron::PolygonizeCopy"
		isNative = True
		class ElectronPolygonizeCopy_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPolyShowFillAll:
		ID = "Electron::PolyShowFillAll"
		isNative = True
		class ElectronPolyShowFillAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPort:
		ID = "Electron::Port"
		isNative = True
		class ElectronPort_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronPrint:
		ID = "Electron::Print"
		isNative = True
		class ElectronPrint_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronQuickRouteAirWire:
		ID = "Electron::QuickRouteAirWire"
		isNative = True
		class ElectronQuickRouteAirWire_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronQuickRouteSignal:
		ID = "Electron::QuickRouteSignal"
		isNative = True
		class ElectronQuickRouteSignal_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronQuickRouteMultiWire:
		ID = "Electron::QuickRouteMultiWire"
		isNative = True
		class ElectronQuickRouteMultiWire_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronQuickRouteSmooth:
		ID = "Electron::QuickRouteSmooth"
		isNative = True
		class ElectronQuickRouteSmooth_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronQuickRouteGuided:
		ID = "Electron::QuickRouteGuided"
		isNative = True
		class ElectronQuickRouteGuided_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRatsnest:
		ID = "Electron::Ratsnest"
		isNative = True
		class ElectronRatsnest_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRectangle:
		ID = "Electron::Rectangle"
		isNative = True
		class ElectronRectangle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRedo:
		ID = "Electron::Redo"
		isNative = True
		class ElectronRedo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronZoomRedraw:
		ID = "Electron::ZoomRedraw"
		isNative = True
		class ElectronZoomRedraw_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRemoveSimModel:
		ID = "Electron::RemoveSimModel"
		isNative = True
		class ElectronRemoveSimModel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronReplace:
		ID = "Electron::Replace"
		isNative = True
		class ElectronReplace_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRepositionAttributes:
		ID = "Electron::RepositionAttributes"
		isNative = True
		class ElectronRepositionAttributes_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronReplaceMissingFonts:
		ID = "Electron::ReplaceMissingFonts"
		isNative = True
		class ElectronReplaceMissingFonts_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronReplaceMissingFontsUseProportional:
		ID = "Electron::ReplaceMissingFontsUseProportional"
		isNative = True
		class ElectronReplaceMissingFontsUseProportional_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronReplaceMissingFontsUseArial:
		ID = "Electron::ReplaceMissingFontsUseArial"
		isNative = True
		class ElectronReplaceMissingFontsUseArial_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronReroute:
		ID = "Electron::Reroute"
		isNative = True
		class ElectronReroute_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipup:
		ID = "Electron::Ripup"
		isNative = True
		class ElectronRipup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupAll:
		ID = "Electron::RipupAll"
		isNative = True
		class ElectronRipupAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupAllPolygons:
		ID = "Electron::RipupAllPolygons"
		isNative = True
		class ElectronRipupAllPolygons_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupConnected:
		ID = "Electron::RipupConnected"
		isNative = True
		class ElectronRipupConnected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupConnectedSameLayer:
		ID = "Electron::RipupConnectedSameLayer"
		isNative = True
		class ElectronRipupConnectedSameLayer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupElementToElement:
		ID = "Electron::RipupElementToElement"
		isNative = True
		class ElectronRipupElementToElement_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRipupSignal:
		ID = "Electron::RipupSignal"
		isNative = True
		class ElectronRipupSignal_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRotate:
		ID = "Electron::Rotate"
		isNative = True
		class ElectronRotate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronManualRoute:
		ID = "Electron::ManualRoute"
		isNative = True
		class ElectronManualRoute_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRouteDiffPair:
		ID = "Electron::RouteDiffPair"
		isNative = True
		class ElectronRouteDiffPair_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRouteMulti:
		ID = "Electron::RouteMulti"
		isNative = True
		class ElectronRouteMulti_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRunULP:
		ID = "Electron::RunULP"
		isNative = True
		class ElectronRunULP_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronRunScript:
		ID = "Electron::RunScript"
		isNative = True
		class ElectronRunScript_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLinkLibrary:
		ID = "Electron::LinkLibrary"
		isNative = True
		class ElectronLinkLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronShow:
		ID = "Electron::Show"
		isNative = True
		class ElectronShow_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSignal:
		ID = "Electron::Signal"
		isNative = True
		class ElectronSignal_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSimulate:
		ID = "Electron::Simulate"
		isNative = True
		class ElectronSimulate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSimOpToggle:
		ID = "Electron::SimOpToggle"
		isNative = True
		class ElectronSimOpToggle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronVProbe:
		ID = "Electron::VProbe"
		isNative = True
		class ElectronVProbe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronVpProbe:
		ID = "Electron::VpProbe"
		isNative = True
		class ElectronVpProbe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSourceSetup:
		ID = "Electron::SourceSetup"
		isNative = True
		class ElectronSourceSetup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronDSourceSetup:
		ID = "Electron::DSourceSetup"
		isNative = True
		class ElectronDSourceSetup_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSlice:
		ID = "Electron::Slice"
		isNative = True
		class ElectronSlice_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSmd:
		ID = "Electron::Smd"
		isNative = True
		class ElectronSmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSmdArray:
		ID = "Electron::SmdArray"
		isNative = True
		class ElectronSmdArray_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSplit:
		ID = "Electron::Split"
		isNative = True
		class ElectronSplit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronStopCommand:
		ID = "Electron::StopCommand"
		isNative = True
		class ElectronStopCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronAddText:
		ID = "Electron::AddText"
		isNative = True
		class ElectronAddText_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronToggleSingleLayer:
		ID = "Electron::ToggleSingleLayer"
		isNative = True
		class ElectronToggleSingleLayer_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUndo:
		ID = "Electron::Undo"
		isNative = True
		class ElectronUndo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUpdateLibrary:
		ID = "Electron::UpdateLibrary"
		isNative = True
		class ElectronUpdateLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronLibraryManager:
		ID = "Electron::LibraryManager"
		isNative = True
		class ElectronLibraryManager_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUpdateDesignFromLibrary:
		ID = "Electron::UpdateDesignFromLibrary"
		isNative = True
		class ElectronUpdateDesignFromLibrary_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronUpdateDesignFromAllLibraries:
		ID = "Electron::UpdateDesignFromAllLibraries"
		isNative = True
		class ElectronUpdateDesignFromAllLibraries_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronValue:
		ID = "Electron::Value"
		isNative = True
		class ElectronValue_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronVariant:
		ID = "Electron::Variant"
		isNative = True
		class ElectronVariant_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronVia:
		ID = "Electron::Via"
		isNative = True
		class ElectronVia_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronWire:
		ID = "Electron::Wire"
		isNative = True
		class ElectronWire_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronZoomIn:
		ID = "Electron::ZoomIn"
		isNative = True
		class ElectronZoomIn_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronZoomOut:
		ID = "Electron::ZoomOut"
		isNative = True
		class ElectronZoomOut_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronZoomRect:
		ID = "Electron::ZoomRect"
		isNative = True
		class ElectronZoomRect_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronZoomToFit:
		ID = "Electron::ZoomToFit"
		isNative = True
		class ElectronZoomToFit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ElectronSynchronize:
		ID = "Electron::Synchronize"
		isNative = True
		class ElectronSynchronize_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFCmnExpandCommand:
		ID = "MSFCmnExpandCommand"
		isNative = True
		class MSFCmnExpandCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFCmnCollapseCommand:
		ID = "MSFCmnCollapseCommand"
		isNative = True
		class MSFCmnCollapseCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestAutoUpdateCmd:
		ID = "MSFNestAutoUpdateCmd"
		isNative = True
	class MAGMatLibraryCmd_Creat:
		ID = "MAGMatLibraryCmd.Creat"
		isNative = True
		class MAGMatLibraryCmd_Creat_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Source:
		ID = "SDK.MAGNestDisplayColorCmd.Source"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Source_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestTranslateCmd_Context:
		ID = "SDK.MAGNestTranslateCmd.Context"
		isNative = True
		class SDK_MAGNestTranslateCmd_Context_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestRefreshCmd_Refresh:
		ID = "SDK.MAGNestRefreshCmd.Refresh"
		isNative = True
		class SDK_MAGNestRefreshCmd_Refresh_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Generate:
		ID = "SDK.MAGNestCalculateCmd.Generate"
		isNative = True
		class SDK_MAGNestCalculateCmd_Generate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_Header:
		ID = "SDK.MAGNestDisplayCmd.Header"
		isNative = True
		class SDK_MAGNestDisplayCmd_Header_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestShapeCmd_Create:
		ID = "SDK.MAGNestShapeCmd.Create"
		isNative = True
		class SDK_MAGNestShapeCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatPropertiesCmd_EditSelected:
		ID = "SDK.MAGFeatPropertiesCmd.EditSelected"
		isNative = True
		class SDK_MAGFeatPropertiesCmd_EditSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestOpenSourceCmd_Open:
		ID = "SDK.MSFNestOpenSourceCmd.Open"
		isNative = True
		class SDK_MSFNestOpenSourceCmd_Open_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestOpenSourceCmd_Open:
		ID = "SDK.MAGNestOpenSourceCmd.Open"
		isNative = True
		class SDK_MAGNestOpenSourceCmd_Open_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestRepresentationCmd_2D:
		ID = "SDK.MAGNestRepresentationCmd.2D"
		isNative = True
		class SDK_MAGNestRepresentationCmd_2D_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestEditNestCmd_Create:
		ID = "SDK.MAGNestEditNestCmd.Create"
		isNative = True
		class SDK_MAGNestEditNestCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestStudyCmd_Context:
		ID = "SDK.MAGNestStudyCmd.Context"
		isNative = True
		class SDK_MAGNestStudyCmd_Context_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatObject_visible_Toggle:
		ID = "SDK.MAGFeatObject.visible.Toggle"
		isNative = True
		class SDK_MAGFeatObject_visible_Toggle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestReportCmd_Show:
		ID = "SDK.MAGNestReportCmd.Show"
		isNative = True
		class SDK_MAGNestReportCmd_Show_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestOnlineOfflineCmd_AddInInv:
		ID = "SDK.MAGNestOnlineOfflineCmd.AddInInv"
		isNative = True
		class SDK_MAGNestOnlineOfflineCmd_AddInInv_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestAutoZoomCmd_inspect:
		ID = "SDK.MAGNestAutoZoomCmd.inspect"
		isNative = True
		class SDK_MAGNestAutoZoomCmd_inspect_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGMatLibraryCmd_CreateNesting:
		ID = "SDK.MAGMatLibraryCmd.CreateNesting"
		isNative = True
		class SDK_MAGMatLibraryCmd_CreateNesting_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatDeleteCmd_DeleteSelected:
		ID = "SDK.MAGFeatDeleteCmd.DeleteSelected"
		isNative = True
		class SDK_MAGFeatDeleteCmd_DeleteSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatCreateFolderCmd_AddToSelected:
		ID = "SDK.MAGFeatCreateFolderCmd.AddToSelected"
		isNative = True
		class SDK_MAGFeatCreateFolderCmd_AddToSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCompareCmd_Compare:
		ID = "SDK.MAGNestCompareCmd.Compare"
		isNative = True
		class SDK_MAGNestCompareCmd_Compare_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_Dimensions:
		ID = "SDK.MAGNestDisplayCmd.Dimensions"
		isNative = True
		class SDK_MAGNestDisplayCmd_Dimensions_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestRepresentationCmd_3DExtrude:
		ID = "SDK.MAGNestRepresentationCmd.3DExtrude"
		isNative = True
		class SDK_MAGNestRepresentationCmd_3DExtrude_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatObject_enabled_Suppress:
		ID = "SDK.MAGFeatObject.enabled.Suppress"
		isNative = True
		class SDK_MAGFeatObject_enabled_Suppress_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestShapeCmd_Edit:
		ID = "SDK.MAGNestShapeCmd.Edit"
		isNative = True
		class SDK_MAGNestShapeCmd_Edit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFCmnFusionLaunchCommand_MSFNestCompareNewCmd:
		ID = "SDK.MSFCmnFusionLaunchCommand.MSFNestCompareNewCmd"
		isNative = True
		class SDK_MSFCmnFusionLaunchCommand_MSFNestCompareNewCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_Shaded:
		ID = "SDK.MAGNestDisplayCmd.Shaded"
		isNative = True
		class SDK_MAGNestDisplayCmd_Shaded_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestRepresentationCmd_3DDetailed:
		ID = "SDK.MAGNestRepresentationCmd.3DDetailed"
		isNative = True
		class SDK_MAGNestRepresentationCmd_3DDetailed_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Mirror:
		ID = "SDK.MAGNestDisplayColorCmd.Mirror"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Mirror_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestExportCmd_FusionExport:
		ID = "SDK.MAGNestExportCmd.FusionExport"
		isNative = True
		class SDK_MAGNestExportCmd_FusionExport_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatUpdateCmd_UpdateAll:
		ID = "SDK.MAGFeatUpdateCmd.UpdateAll"
		isNative = True
		class SDK_MAGFeatUpdateCmd_UpdateAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Stop:
		ID = "SDK.MAGNestCalculateCmd.Stop"
		isNative = True
		class SDK_MAGNestCalculateCmd_Stop_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestProvidersCmd_Config:
		ID = "SDK.MAGNestProvidersCmd.Config"
		isNative = True
		class SDK_MAGNestProvidersCmd_Config_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGTestMainCommand_Test:
		ID = "SDK.MAGTestMainCommand.Test"
		isNative = True
		class SDK_MAGTestMainCommand_Test_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestBindUnbindPropertyCmd_ShapeBindAll:
		ID = "SDK.MAGNestBindUnbindPropertyCmd.ShapeBindAll"
		isNative = True
		class SDK_MAGNestBindUnbindPropertyCmd_ShapeBindAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestCreateWorkingModelCmd_Create:
		ID = "SDK.MSFNestCreateWorkingModelCmd.Create"
		isNative = True
		class SDK_MSFNestCreateWorkingModelCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSelectionCmd_Contours:
		ID = "SDK.MAGNestSelectionCmd.Contours"
		isNative = True
		class SDK_MAGNestSelectionCmd_Contours_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestViewCmd_Next:
		ID = "SDK.MAGNestViewCmd.Next"
		isNative = True
		class SDK_MAGNestViewCmd_Next_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestBindUnbindPropertyCmd_NestItemBindAll:
		ID = "SDK.MAGNestBindUnbindPropertyCmd.NestItemBindAll"
		isNative = True
		class SDK_MAGNestBindUnbindPropertyCmd_NestItemBindAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSelectionCmd_Sources:
		ID = "SDK.MAGNestSelectionCmd.Sources"
		isNative = True
		class SDK_MAGNestSelectionCmd_Sources_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestShowTranslateErrorDlgCmd_Show:
		ID = "SDK.MAGNestShowTranslateErrorDlgCmd.Show"
		isNative = True
		class SDK_MAGNestShowTranslateErrorDlgCmd_Show_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestAutoCreateKitsCmd_Create:
		ID = "SDK.MAGNestAutoCreateKitsCmd.Create"
		isNative = True
		class SDK_MAGNestAutoCreateKitsCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_SheetConstructionPoint:
		ID = "SDK.MAGNestDisplayCmd.SheetConstructionPoint"
		isNative = True
		class SDK_MAGNestDisplayCmd_SheetConstructionPoint_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestRepresentationCmd_3DCompare:
		ID = "SDK.MAGNestRepresentationCmd.3DCompare"
		isNative = True
		class SDK_MAGNestRepresentationCmd_3DCompare_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Calculate:
		ID = "SDK.MAGNestCalculateCmd.Calculate"
		isNative = True
		class SDK_MAGNestCalculateCmd_Calculate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGMatLibraryCmd_Create:
		ID = "SDK.MAGMatLibraryCmd.Create"
		isNative = True
		class SDK_MAGMatLibraryCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestInfoPanelCmd_Show:
		ID = "SDK.MAGNestInfoPanelCmd.Show"
		isNative = True
		class SDK_MAGNestInfoPanelCmd_Show_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestKitsCmd_Edit:
		ID = "SDK.MAGNestKitsCmd.Edit"
		isNative = True
		class SDK_MAGNestKitsCmd_Edit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestAutoZoomCmd_select:
		ID = "SDK.MAGNestAutoZoomCmd.select"
		isNative = True
		class SDK_MAGNestAutoZoomCmd_select_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_SheetGeometry:
		ID = "SDK.MAGNestDisplayCmd.SheetGeometry"
		isNative = True
		class SDK_MAGNestDisplayCmd_SheetGeometry_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGTestOptionsCmd_Test:
		ID = "SDK.MAGTestOptionsCmd.Test"
		isNative = True
		class SDK_MAGTestOptionsCmd_Test_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Material:
		ID = "SDK.MAGNestDisplayColorCmd.Material"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Material_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestCreateF3DCmd_Create:
		ID = "SDK.MSFNestCreateF3DCmd.Create"
		isNative = True
		class SDK_MSFNestCreateF3DCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestBindUnbindPropertyCmd_NestItemUnbindAll:
		ID = "SDK.MAGNestBindUnbindPropertyCmd.NestItemUnbindAll"
		isNative = True
		class SDK_MAGNestBindUnbindPropertyCmd_NestItemUnbindAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestExportCmd_Export:
		ID = "SDK.MAGNestExportCmd.Export"
		isNative = True
		class SDK_MAGNestExportCmd_Export_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSaveCmd_SaveAll:
		ID = "SDK.MAGNestSaveCmd.SaveAll"
		isNative = True
		class SDK_MAGNestSaveCmd_SaveAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSelectionCmd_Segments:
		ID = "SDK.MAGNestSelectionCmd.Segments"
		isNative = True
		class SDK_MAGNestSelectionCmd_Segments_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestShapeCmd_Context:
		ID = "SDK.MAGNestShapeCmd.Context"
		isNative = True
		class SDK_MAGNestShapeCmd_Context_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestStudyCmd_Create:
		ID = "SDK.MAGNestStudyCmd.Create"
		isNative = True
		class SDK_MAGNestStudyCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatUpdateCmd_UpdateAllTruNest:
		ID = "SDK.MAGFeatUpdateCmd.UpdateAllTruNest"
		isNative = True
		class SDK_MAGFeatUpdateCmd_UpdateAllTruNest_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatUpdateCmd_AutoUpdateNoDelay:
		ID = "SDK.MAGFeatUpdateCmd.AutoUpdateNoDelay"
		isNative = True
		class SDK_MAGFeatUpdateCmd_AutoUpdateNoDelay_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_Geometry:
		ID = "SDK.MAGNestDisplayCmd.Geometry"
		isNative = True
		class SDK_MAGNestDisplayCmd_Geometry_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatOpenExternalLinkCmd_Open:
		ID = "SDK.MAGFeatOpenExternalLinkCmd.Open"
		isNative = True
		class SDK_MAGFeatOpenExternalLinkCmd_Open_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Save:
		ID = "SDK.MAGNestCalculateCmd.Save"
		isNative = True
		class SDK_MAGNestCalculateCmd_Save_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_ConstructionPoint:
		ID = "SDK.MAGNestDisplayCmd.ConstructionPoint"
		isNative = True
		class SDK_MAGNestDisplayCmd_ConstructionPoint_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestExportCachedDxfCmd_Export:
		ID = "SDK.MAGNestExportCachedDxfCmd.Export"
		isNative = True
		class SDK_MAGNestExportCachedDxfCmd_Export_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_ExtraConstructionPoint:
		ID = "SDK.MAGNestDisplayCmd.ExtraConstructionPoint"
		isNative = True
		class SDK_MAGNestDisplayCmd_ExtraConstructionPoint_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestTranslateCmd_ContextExtract:
		ID = "SDK.MAGNestTranslateCmd.ContextExtract"
		isNative = True
		class SDK_MAGNestTranslateCmd_ContextExtract_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_SheetText:
		ID = "SDK.MAGNestDisplayCmd.SheetText"
		isNative = True
		class SDK_MAGNestDisplayCmd_SheetText_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestViewCmd_First:
		ID = "SDK.MAGNestViewCmd.First"
		isNative = True
		class SDK_MAGNestViewCmd_First_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFCmnFusionLaunchCommand_CompareCmd:
		ID = "SDK.MSFCmnFusionLaunchCommand.CompareCmd"
		isNative = True
		class SDK_MSFCmnFusionLaunchCommand_CompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Cancel:
		ID = "SDK.MAGNestCalculateCmd.Cancel"
		isNative = True
		class SDK_MAGNestCalculateCmd_Cancel_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestBindUnbindPropertyCmd_ShapeUnbindAll:
		ID = "SDK.MAGNestBindUnbindPropertyCmd.ShapeUnbindAll"
		isNative = True
		class SDK_MAGNestBindUnbindPropertyCmd_ShapeUnbindAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatAutoZoomCmd_Create:
		ID = "SDK.MAGFeatAutoZoomCmd.Create"
		isNative = True
		class SDK_MAGFeatAutoZoomCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatDuplicateCmd_DuplicateSelected:
		ID = "SDK.MAGFeatDuplicateCmd.DuplicateSelected"
		isNative = True
		class SDK_MAGFeatDuplicateCmd_DuplicateSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatUpdateCmd_UpdateSelection:
		ID = "SDK.MAGFeatUpdateCmd.UpdateSelection"
		isNative = True
		class SDK_MAGFeatUpdateCmd_UpdateSelection_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Segment:
		ID = "SDK.MAGNestDisplayColorCmd.Segment"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Segment_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestTranslateCmd_Create:
		ID = "SDK.MAGNestTranslateCmd.Create"
		isNative = True
		class SDK_MAGNestTranslateCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatObject_enabled_Toggle:
		ID = "SDK.MAGFeatObject.enabled.Toggle"
		isNative = True
		class SDK_MAGFeatObject_enabled_Toggle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_ExtraText:
		ID = "SDK.MAGNestDisplayCmd.ExtraText"
		isNative = True
		class SDK_MAGNestDisplayCmd_ExtraText_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSelectionCmd_Shapes:
		ID = "SDK.MAGNestSelectionCmd.Shapes"
		isNative = True
		class SDK_MAGNestSelectionCmd_Shapes_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatCopyCmd_CopySelected:
		ID = "SDK.MAGFeatCopyCmd.CopySelected"
		isNative = True
		class SDK_MAGFeatCopyCmd_CopySelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestSaveContainerDataCmd_Create:
		ID = "SDK.MSFNestSaveContainerDataCmd.Create"
		isNative = True
		class SDK_MSFNestSaveContainerDataCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatRenameCmd_RenameSelected:
		ID = "SDK.MAGFeatRenameCmd.RenameSelected"
		isNative = True
		class SDK_MAGFeatRenameCmd_RenameSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestEditNestCmd_Edit:
		ID = "SDK.MAGNestEditNestCmd.Edit"
		isNative = True
		class SDK_MAGNestEditNestCmd_Edit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestViewCmd_Previous:
		ID = "SDK.MAGNestViewCmd.Previous"
		isNative = True
		class SDK_MAGNestViewCmd_Previous_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Default:
		ID = "SDK.MAGNestDisplayColorCmd.Default"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Default_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_Shape:
		ID = "SDK.MAGNestDisplayColorCmd.Shape"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_Shape_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_Start:
		ID = "SDK.MAGNestCalculateCmd.Start"
		isNative = True
		class SDK_MAGNestCalculateCmd_Start_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_ExtraGeometry:
		ID = "SDK.MAGNestDisplayCmd.ExtraGeometry"
		isNative = True
		class SDK_MAGNestDisplayCmd_ExtraGeometry_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestAutoZoomCmd_off:
		ID = "SDK.MAGNestAutoZoomCmd.off"
		isNative = True
		class SDK_MAGNestAutoZoomCmd_off_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestSelectionCmd_Sheets:
		ID = "SDK.MAGNestSelectionCmd.Sheets"
		isNative = True
		class SDK_MAGNestSelectionCmd_Sheets_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_FabricationInfo:
		ID = "SDK.MAGNestDisplayCmd.FabricationInfo"
		isNative = True
		class SDK_MAGNestDisplayCmd_FabricationInfo_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatDefaultFolderCmd_SetDefault:
		ID = "SDK.MAGFeatDefaultFolderCmd.SetDefault"
		isNative = True
		class SDK_MAGFeatDefaultFolderCmd_SetDefault_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestAutoZoomCmd_toggle:
		ID = "SDK.MAGNestAutoZoomCmd.toggle"
		isNative = True
		class SDK_MAGNestAutoZoomCmd_toggle_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestKitsCmd_Create:
		ID = "SDK.MAGNestKitsCmd.Create"
		isNative = True
		class SDK_MAGNestKitsCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatPasteCmd_PasteCopied:
		ID = "SDK.MAGFeatPasteCmd.PasteCopied"
		isNative = True
		class SDK_MAGFeatPasteCmd_PasteCopied_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestGeoSourcesCmd_Delete:
		ID = "SDK.MAGNestGeoSourcesCmd.Delete"
		isNative = True
		class SDK_MAGNestGeoSourcesCmd_Delete_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatUpdateCmd_AutoUpdate:
		ID = "SDK.MAGFeatUpdateCmd.AutoUpdate"
		isNative = True
		class SDK_MAGFeatUpdateCmd_AutoUpdate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestInfoPanelCmd_Context:
		ID = "SDK.MAGNestInfoPanelCmd.Context"
		isNative = True
		class SDK_MAGNestInfoPanelCmd_Context_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestViewCmd_Last:
		ID = "SDK.MAGNestViewCmd.Last"
		isNative = True
		class SDK_MAGNestViewCmd_Last_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_SourceOrientation:
		ID = "SDK.MAGNestDisplayColorCmd.SourceOrientation"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_SourceOrientation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestStudyCmd_Edit:
		ID = "SDK.MAGNestStudyCmd.Edit"
		isNative = True
		class SDK_MAGNestStudyCmd_Edit_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestMSIFileToF3DCmd_Import:
		ID = "SDK.MSFNestMSIFileToF3DCmd.Import"
		isNative = True
		class SDK_MSFNestMSIFileToF3DCmd_Import_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestCalculateCmd_SaveAll:
		ID = "SDK.MAGNestCalculateCmd.SaveAll"
		isNative = True
		class SDK_MAGNestCalculateCmd_SaveAll_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestGeoSourcesCmd_Show:
		ID = "SDK.MAGNestGeoSourcesCmd.Show"
		isNative = True
		class SDK_MAGNestGeoSourcesCmd_Show_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestUpdateAssemblyProviderCmd_Update:
		ID = "SDK.MAGNestUpdateAssemblyProviderCmd.Update"
		isNative = True
		class SDK_MAGNestUpdateAssemblyProviderCmd_Update_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MSFNestDeleteCmd_DeleteSelected:
		ID = "SDK.MSFNestDeleteCmd.DeleteSelected"
		isNative = True
		class SDK_MSFNestDeleteCmd_DeleteSelected_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestGeoSourcesCmd_Hide:
		ID = "SDK.MAGNestGeoSourcesCmd.Hide"
		isNative = True
		class SDK_MAGNestGeoSourcesCmd_Hide_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGFeatAutoUpdateCmd_AddInNestingUtility:
		ID = "SDK.MAGFeatAutoUpdateCmd.AddInNestingUtility"
		isNative = True
		class SDK_MAGFeatAutoUpdateCmd_AddInNestingUtility_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayCmd_Wireframe:
		ID = "SDK.MAGNestDisplayCmd.Wireframe"
		isNative = True
		class SDK_MAGNestDisplayCmd_Wireframe_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGNestDisplayColorCmd_NestedOrientation:
		ID = "SDK.MAGNestDisplayColorCmd.NestedOrientation"
		isNative = True
		class SDK_MAGNestDisplayColorCmd_NestedOrientation_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class SDK_MAGMatLibraryCmd_FusionNesting:
		ID = "SDK.MAGMatLibraryCmd.FusionNesting"
		isNative = True
		class SDK_MAGMatLibraryCmd_FusionNesting_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestRemoveAggregateCompCmd:
		ID = "MSFNestRemoveAggregateCompCmd"
		isNative = True
		class MSFNestRemoveAggregateCompCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestAuthoringCmd:
		ID = "MSFNestAuthoringCmd"
		isNative = True
		class MSFNestAuthoringCmd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ImportTruNestMSI:
		ID = "ImportTruNestMSI"
		isNative = True
		class ImportTruNestMSI_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ExportTruNestMSI:
		ID = "ExportTruNestMSI"
		isNative = True
		class ExportTruNestMSI_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestSourcesCmd:
		ID = "MSFNestSourcesCmd"
		isNative = True
		class MSFNestSourcesCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestShapeCmd:
		ID = "MSFNestShapeCmd"
		isNative = True
		class MSFNestShapeCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestCreateStudyCmd:
		ID = "MSFNestCreateStudyCmd"
		isNative = True
		class MSFNestCreateStudyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestEditStudyCmd:
		ID = "MSFNestEditStudyCmd"
		isNative = True
		class MSFNestEditStudyCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class CompareCmd:
		ID = "CompareCmd"
		isNative = True
		class CompareCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestShowSheetItemsCmd:
		ID = "MSFNestShowSheetItemsCmd"
		isNative = True
		class MSFNestShowSheetItemsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestPartLabelInfoCmd:
		ID = "MSFNestPartLabelInfoCmd"
		isNative = True
		class MSFNestPartLabelInfoCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestEditNestCmd:
		ID = "MSFNestEditNestCmd"
		isNative = True
		class MSFNestEditNestCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestCompareNewCmd:
		ID = "MSFNestCompareNewCmd"
		isNative = True
		class MSFNestCompareNewCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestSyncNestCmd:
		ID = "MSFNestSyncNestCmd"
		isNative = True
		class MSFNestSyncNestCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestPrepareNestCmd:
		ID = "MSFNestPrepareNestCmd"
		isNative = True
		class MSFNestPrepareNestCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestSyncAggregationCmd:
		ID = "MSFNestSyncAggregationCmd"
		isNative = True
		class MSFNestSyncAggregationCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestInitializeEnvironmentCmd:
		ID = "MSFNestInitializeEnvironmentCmd"
		isNative = True
		class MSFNestInitializeEnvironmentCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestSyncWorkingModelsCmd:
		ID = "MSFNestSyncWorkingModelsCmd"
		isNative = True
		class MSFNestSyncWorkingModelsCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSFNestNameConventionCmd:
		ID = "MSFNestNameConventionCmd"
		isNative = True
		class MSFNestNameConventionCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSF_MAGMatLibraryCmd_FusionNesting:
		ID = "MSF.MAGMatLibraryCmd.FusionNesting"
		isNative = True
		class MSF_MAGMatLibraryCmd_FusionNesting_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSF_MAGNestCalculateCmd_Generate:
		ID = "MSF.MAGNestCalculateCmd.Generate"
		isNative = True
		class MSF_MAGNestCalculateCmd_Generate_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class MSF_MSFNestSaveContainerDataCmd_Create:
		ID = "MSF.MSFNestSaveContainerDataCmd.Create"
		isNative = True
		class MSF_MSFNestSaveContainerDataCmd_Create_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshInsertCommand:
		ID = "ParaMeshInsertCommand"
		isNative = True
		class ParaMeshInsertCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshExportCommand:
		ID = "ParaMeshExportCommand"
		isNative = True
		class ParaMeshExportCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshAdoptCommand:
		ID = "ParaMeshAdoptCommand"
		isNative = True
		class ParaMeshAdoptCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDemoteCommand:
		ID = "ParaMeshDemoteCommand"
		isNative = True
		class ParaMeshDemoteCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshTessellateCommand:
		ID = "ParaMeshTessellateCommand"
		isNative = True
		class ParaMeshTessellateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcTessellateEditCommand:
		ID = "ParaMeshDcTessellateEditCommand"
		isNative = True
		class ParaMeshDcTessellateEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshSmoothCommand:
		ID = "ParaMeshSmoothCommand"
		isNative = True
		class ParaMeshSmoothCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcSmoothEditCommand:
		ID = "ParaMeshDcSmoothEditCommand"
		isNative = True
		class ParaMeshDcSmoothEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshLatticeCommand:
		ID = "ParaMeshLatticeCommand"
		isNative = True
		class ParaMeshLatticeCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcLatticeEditCommand:
		ID = "ParaMeshDcLatticeEditCommand"
		isNative = True
		class ParaMeshDcLatticeEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshReduceCommand:
		ID = "ParaMeshReduceCommand"
		isNative = True
		class ParaMeshReduceCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcReduceEditCommand:
		ID = "ParaMeshDcReduceEditCommand"
		isNative = True
		class ParaMeshDcReduceEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshCombineCommand:
		ID = "ParaMeshCombineCommand"
		isNative = True
		class ParaMeshCombineCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcCombineEditCommand:
		ID = "ParaMeshDcCombineEditCommand"
		isNative = True
		class ParaMeshDcCombineEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshRepairCommand:
		ID = "ParaMeshRepairCommand"
		isNative = True
		class ParaMeshRepairCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcRepairEditCommand:
		ID = "ParaMeshDcRepairEditCommand"
		isNative = True
		class ParaMeshDcRepairEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshHollowCommand:
		ID = "ParaMeshHollowCommand"
		isNative = True
		class ParaMeshHollowCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcHollowEditCommand:
		ID = "ParaMeshDcHollowEditCommand"
		isNative = True
		class ParaMeshDcHollowEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshRemeshCommand:
		ID = "ParaMeshRemeshCommand"
		isNative = True
		class ParaMeshRemeshCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcRemeshEditCommand:
		ID = "ParaMeshDcRemeshEditCommand"
		isNative = True
		class ParaMeshDcRemeshEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshReverseNormalsCommand:
		ID = "ParaMeshReverseNormalsCommand"
		isNative = True
		class ParaMeshReverseNormalsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcReverseNormalsEditCommand:
		ID = "ParaMeshDcReverseNormalsEditCommand"
		isNative = True
		class ParaMeshDcReverseNormalsEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshMergeFaceGroupsCommand:
		ID = "ParaMeshMergeFaceGroupsCommand"
		isNative = True
		class ParaMeshMergeFaceGroupsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcMergeFaceGroupsEditCommand:
		ID = "ParaMeshDcMergeFaceGroupsEditCommand"
		isNative = True
		class ParaMeshDcMergeFaceGroupsEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshPlaneCutCommand:
		ID = "ParaMeshPlaneCutCommand"
		isNative = True
		class ParaMeshPlaneCutCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcPlaneCutEditCommand:
		ID = "ParaMeshDcPlaneCutEditCommand"
		isNative = True
		class ParaMeshDcPlaneCutEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshToQuadMeshCommand:
		ID = "ParaMeshToQuadMeshCommand"
		isNative = True
		class ParaMeshToQuadMeshCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcToQuadMeshEditCommand:
		ID = "ParaMeshDcToQuadMeshEditCommand"
		isNative = True
		class ParaMeshDcToQuadMeshEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshConvertCommand:
		ID = "ParaMeshConvertCommand"
		isNative = True
		class ParaMeshConvertCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcConvertEditCommand:
		ID = "ParaMeshDcConvertEditCommand"
		isNative = True
		class ParaMeshDcConvertEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshExtractCommand:
		ID = "ParaMeshExtractCommand"
		isNative = True
		class ParaMeshExtractCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcExtractEditCommand:
		ID = "ParaMeshDcExtractEditCommand"
		isNative = True
		class ParaMeshDcExtractEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshCalculateFaceGroupsCommand:
		ID = "ParaMeshCalculateFaceGroupsCommand"
		isNative = True
		class ParaMeshCalculateFaceGroupsCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcCalculateFaceGroupsEditCommand:
		ID = "ParaMeshDcCalculateFaceGroupsEditCommand"
		isNative = True
		class ParaMeshDcCalculateFaceGroupsEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcMoveCopyEditCommand:
		ID = "ParaMeshDcMoveCopyEditCommand"
		isNative = True
		class ParaMeshDcMoveCopyEditCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshScaleCommand:
		ID = "ParaMeshScaleCommand"
		isNative = True
		class ParaMeshScaleCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcScaleEditCommand:
		ID = "ParaMeshDcScaleEditCommand"
		isNative = True
		class ParaMeshDcScaleEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshRemoveCommand:
		ID = "ParaMeshRemoveCommand"
		isNative = True
		class ParaMeshRemoveCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshPlanarSectionCommand:
		ID = "ParaMeshPlanarSectionCommand"
		isNative = True
		class ParaMeshPlanarSectionCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshDcPlanarSectionEditCommand:
		ID = "ParaMeshDcPlanarSectionEditCommand"
		isNative = True
		class ParaMeshDcPlanarSectionEditCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshBaseFeatureCreateCommand:
		ID = "ParaMeshBaseFeatureCreateCommand"
		isNative = True
		class ParaMeshBaseFeatureCreateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshBaseFeatureActivateCommand:
		ID = "ParaMeshBaseFeatureActivateCommand"
		isNative = True
		class ParaMeshBaseFeatureActivateCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshBaseFeatureStopCommand:
		ID = "ParaMeshBaseFeatureStopCommand"
		isNative = True
		class ParaMeshBaseFeatureStopCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshCreateFaceGroupCommand:
		ID = "ParaMeshCreateFaceGroupCommand"
		isNative = True
		class ParaMeshCreateFaceGroupCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshEraseAndFillCommand:
		ID = "ParaMeshEraseAndFillCommand"
		isNative = True
		class ParaMeshEraseAndFillCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshInsertAlignCommand:
		ID = "ParaMeshInsertAlignCommand"
		isNative = True
		class ParaMeshInsertAlignCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshPositionCommand:
		ID = "ParaMeshPositionCommand"
		isNative = True
		class ParaMeshPositionCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshShowSelectionPanelCmd:
		ID = "ParaMeshShowSelectionPanelCmd"
		isNative = True
		class ParaMeshShowSelectionPanelCmd_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "CheckBoxControlDefinition"
	class ParaMeshFlatMeshShadingCommand:
		ID = "ParaMeshFlatMeshShadingCommand"
		isNative = True
		class ParaMeshFlatMeshShadingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ParaMeshSmoothMeshShadingCommand:
		ID = "ParaMeshSmoothMeshShadingCommand"
		isNative = True
		class ParaMeshSmoothMeshShadingCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class DiagnosticsCommand:
		ID = "DiagnosticsCommand"
		isNative = True
		class DiagnosticsCommand_control:
			isVisible = False
			isEnabled = False
			DefinitionType = "ButtonControlDefinition"
	class PackageGenerator:
		ID = "PackageGenerator"
		isNative = False
		class PackageGenerator_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Axial:
		ID = "cmd_id_Axial"
		isNative = False
		class cmd_id_Axial_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_BGA:
		ID = "cmd_id_BGA"
		isNative = False
		class cmd_id_BGA_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Chip:
		ID = "cmd_id_Chip"
		isNative = False
		class cmd_id_Chip_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Soic:
		ID = "cmd_id_Soic"
		isNative = False
		class cmd_id_Soic_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_DFN2:
		ID = "cmd_id_DFN2"
		isNative = False
		class cmd_id_DFN2_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_DFN3:
		ID = "cmd_id_DFN3"
		isNative = False
		class cmd_id_DFN3_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_DFN4:
		ID = "cmd_id_DFN4"
		isNative = False
		class cmd_id_DFN4_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_header_right_angle:
		ID = "cmd_id_header_right_angle"
		isNative = False
		class cmd_id_header_right_angle_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_header_right_angle_socket:
		ID = "cmd_id_header_right_angle_socket"
		isNative = False
		class cmd_id_header_right_angle_socket_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_header_straight:
		ID = "cmd_id_header_straight"
		isNative = False
		class cmd_id_header_straight_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_header_straight_socket:
		ID = "cmd_id_header_straight_socket"
		isNative = False
		class cmd_id_header_straight_socket_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Son:
		ID = "cmd_id_Son"
		isNative = False
		class cmd_id_Son_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Chip_led:
		ID = "cmd_id_Chip_led"
		isNative = False
		class cmd_id_Chip_led_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Qfp:
		ID = "cmd_id_Qfp"
		isNative = False
		class cmd_id_Qfp_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Qfn:
		ID = "cmd_id_Qfn"
		isNative = False
		class cmd_id_Qfn_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_chiparray_2side_convex:
		ID = "cmd_id_chiparray_2side_convex"
		isNative = False
		class cmd_id_chiparray_2side_convex_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_chiparray_2side_flat_concave:
		ID = "cmd_id_chiparray_2side_flat_concave"
		isNative = False
		class cmd_id_chiparray_2side_flat_concave_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_chiparray_4side_flat:
		ID = "cmd_id_chiparray_4side_flat"
		isNative = False
		class cmd_id_chiparray_4side_flat_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_sot143:
		ID = "cmd_id_sot143"
		isNative = False
		class cmd_id_sot143_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_sot223:
		ID = "cmd_id_sot223"
		isNative = False
		class cmd_id_sot223_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_sot23:
		ID = "cmd_id_sot23"
		isNative = False
		class cmd_id_sot23_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_sotfl:
		ID = "cmd_id_sotfl"
		isNative = False
		class cmd_id_sotfl_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Plcc:
		ID = "cmd_id_Plcc"
		isNative = False
		class cmd_id_Plcc_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Oscillator_j:
		ID = "cmd_id_Oscillator_j"
		isNative = False
		class cmd_id_Oscillator_j_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Oscillator_l:
		ID = "cmd_id_Oscillator_l"
		isNative = False
		class cmd_id_Oscillator_l_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Soj:
		ID = "cmd_id_Soj"
		isNative = False
		class cmd_id_Soj_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_crystal:
		ID = "cmd_id_crystal"
		isNative = False
		class cmd_id_crystal_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_crystal_hc49:
		ID = "cmd_id_crystal_hc49"
		isNative = False
		class cmd_id_crystal_hc49_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_dip:
		ID = "cmd_id_dip"
		isNative = False
		class cmd_id_dip_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_ecap:
		ID = "cmd_id_ecap"
		isNative = False
		class cmd_id_ecap_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Melf:
		ID = "cmd_id_Melf"
		isNative = False
		class cmd_id_Melf_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Molded:
		ID = "cmd_id_Molded"
		isNative = False
		class cmd_id_Molded_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_female_standoff:
		ID = "cmd_id_female_standoff"
		isNative = False
		class cmd_id_female_standoff_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_male_female_standoff:
		ID = "cmd_id_male_female_standoff"
		isNative = False
		class cmd_id_male_female_standoff_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Sod:
		ID = "cmd_id_Sod"
		isNative = False
		class cmd_id_Sod_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Snaplock:
		ID = "cmd_id_Snaplock"
		isNative = False
		class cmd_id_Snaplock_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Radial:
		ID = "cmd_id_Radial"
		isNative = False
		class cmd_id_Radial_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Radial_Round_Led:
		ID = "cmd_id_Radial_Round_Led"
		isNative = False
		class cmd_id_Radial_Round_Led_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Cornerconcave:
		ID = "cmd_id_Cornerconcave"
		isNative = False
		class cmd_id_Cornerconcave_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_Sodfl:
		ID = "cmd_id_Sodfl"
		isNative = False
		class cmd_id_Sodfl_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_TODPAK:
		ID = "cmd_id_TODPAK"
		isNative = False
		class cmd_id_TODPAK_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_surafce_mount_header_female:
		ID = "cmd_id_surafce_mount_header_female"
		isNative = False
		class cmd_id_surafce_mount_header_female_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmd_id_surface_mount_pin_header_male:
		ID = "cmd_id_surface_mount_pin_header_male"
		isNative = False
		class cmd_id_surface_mount_pin_header_male_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cadenasparts4cad:
		ID = "cadenasparts4cad"
		isNative = False
		class cadenasparts4cad_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class traceparts_insert:
		ID = "traceparts_insert"
		isNative = False
		class traceparts_insert_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutPremadeDropdown:
		ID = "thomasa88_anyShortcutPremadeDropdown"
		isNative = False
		class thomasa88_anyShortcutPremadeDropdown_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class thomasa88_anyShortcutListLookAtSketchCommand:
		ID = "thomasa88_anyShortcutListLookAtSketchCommand"
		isNative = False
		class thomasa88_anyShortcutListLookAtSketchCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutListLookAtSketchOrSelectedCommand:
		ID = "thomasa88_anyShortcutListLookAtSketchOrSelectedCommand"
		isNative = False
		class thomasa88_anyShortcutListLookAtSketchOrSelectedCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutListActivateContainingOrComponentCommand:
		ID = "thomasa88_anyShortcutListActivateContainingOrComponentCommand"
		isNative = False
		class thomasa88_anyShortcutListActivateContainingOrComponentCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinRepeatCommand:
		ID = "thomasa88_anyShortcutBuiltinRepeatCommand"
		isNative = False
		class thomasa88_anyShortcutBuiltinRepeatCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinTimelineList:
		ID = "thomasa88_anyShortcutBuiltinTimelineList"
		isNative = False
		class thomasa88_anyShortcutBuiltinTimelineList_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class thomasa88_anyShortcutListRollToBeginning:
		ID = "thomasa88_anyShortcutListRollToBeginning"
		isNative = False
		class thomasa88_anyShortcutListRollToBeginning_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutListRollBack:
		ID = "thomasa88_anyShortcutListRollBack"
		isNative = False
		class thomasa88_anyShortcutListRollBack_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutListRollForward:
		ID = "thomasa88_anyShortcutListRollForward"
		isNative = False
		class thomasa88_anyShortcutListRollForward_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutListRollToEnd:
		ID = "thomasa88_anyShortcutListRollToEnd"
		isNative = False
		class thomasa88_anyShortcutListRollToEnd_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewList:
		ID = "thomasa88_anyShortcutBuiltinViewList"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewList_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class thomasa88_anyShortcutBuiltinViewFront:
		ID = "thomasa88_anyShortcutBuiltinViewFront"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewFront_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewBack:
		ID = "thomasa88_anyShortcutBuiltinViewBack"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewBack_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewTop:
		ID = "thomasa88_anyShortcutBuiltinViewTop"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewTop_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewBottom:
		ID = "thomasa88_anyShortcutBuiltinViewBottom"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewBottom_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewLeft:
		ID = "thomasa88_anyShortcutBuiltinViewLeft"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewLeft_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutBuiltinViewRight:
		ID = "thomasa88_anyShortcutBuiltinViewRight"
		isNative = False
		class thomasa88_anyShortcutBuiltinViewRight_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class thomasa88_anyShortcutDropdown:
		ID = "thomasa88_anyShortcutDropdown"
		isNative = False
		class thomasa88_anyShortcutDropdown_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class thomasa88_anyShortcutList:
		ID = "thomasa88_anyShortcutList"
		isNative = False
		class thomasa88_anyShortcutList_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC1:
		ID = "NC1"
		isNative = False
		class NC1_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC2:
		ID = "NC2"
		isNative = False
		class NC2_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC3:
		ID = "NC3"
		isNative = False
		class NC3_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC4:
		ID = "NC4"
		isNative = False
		class NC4_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC5:
		ID = "NC5"
		isNative = False
		class NC5_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC6:
		ID = "NC6"
		isNative = False
		class NC6_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC7:
		ID = "NC7"
		isNative = False
		class NC7_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC8:
		ID = "NC8"
		isNative = False
		class NC8_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC9:
		ID = "NC9"
		isNative = False
		class NC9_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC10:
		ID = "NC10"
		isNative = False
		class NC10_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class NC11:
		ID = "NC11"
		isNative = False
		class NC11_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class ExportToUnity_hellion:
		ID = "ExportToUnity_hellion"
		isNative = False
		class ExportToUnity_hellion_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersrootDropdown:
		ID = "OpenFoldersrootDropdown"
		isNative = False
		class OpenFoldersrootDropdown_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class OpenFoldersrootDropdownUndoc:
		ID = "OpenFoldersrootDropdownUndoc"
		isNative = False
		class OpenFoldersrootDropdownUndoc_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class thomasa88_NoComponentDrag_Enable:
		ID = "thomasa88_NoComponentDrag_Enable"
		isNative = False
		class thomasa88_NoComponentDrag_Enable_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "CheckBoxControlDefinition"
	class cmdID_demo_1:
		ID = "cmdID_demo_1"
		isNative = False
		class cmdID_demo_1_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmdID_PolyhedaCommand:
		ID = "cmdID_PolyhedaCommand"
		isNative = False
		class cmdID_PolyhedaCommand_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class cmdID_HexNut:
		ID = "cmdID_HexNut"
		isNative = False
		class cmdID_HexNut_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersFusionInstall:
		ID = "OpenFoldersFusionInstall"
		isNative = False
		class OpenFoldersFusionInstall_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersFusionApi:
		ID = "OpenFoldersFusionApi"
		isNative = False
		class OpenFoldersFusionApi_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class OpenFoldersFusionApiCpp:
		ID = "OpenFoldersFusionApiCpp"
		isNative = False
		class OpenFoldersFusionApiCpp_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersFusionApiPython:
		ID = "OpenFoldersFusionApiPython"
		isNative = False
		class OpenFoldersFusionApiPython_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersFusionPython:
		ID = "OpenFoldersFusionPython"
		isNative = False
		class OpenFoldersFusionPython_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAutodesk:
		ID = "OpenFoldersAutodesk"
		isNative = False
		class OpenFoldersAutodesk_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class OpenFoldersAutodeskLocal:
		ID = "OpenFoldersAutodeskLocal"
		isNative = False
		class OpenFoldersAutodeskLocal_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAutodeskRoaming:
		ID = "OpenFoldersAutodeskRoaming"
		isNative = False
		class OpenFoldersAutodeskRoaming_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersDesktop:
		ID = "OpenFoldersDesktop"
		isNative = False
		class OpenFoldersDesktop_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersTempFiles:
		ID = "OpenFoldersTempFiles"
		isNative = False
		class OpenFoldersTempFiles_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAppdata:
		ID = "OpenFoldersAppdata"
		isNative = False
		class OpenFoldersAppdata_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "StandardListControlDefinition"
	class OpenFoldersAppdataLocal:
		ID = "OpenFoldersAppdataLocal"
		isNative = False
		class OpenFoldersAppdataLocal_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAppdataRoaming:
		ID = "OpenFoldersAppdataRoaming"
		isNative = False
		class OpenFoldersAppdataRoaming_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersSettings:
		ID = "OpenFoldersSettings"
		isNative = False
		class OpenFoldersSettings_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersRootDirectory:
		ID = "OpenFoldersRootDirectory"
		isNative = False
		class OpenFoldersRootDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersExecutableDirectory:
		ID = "OpenFoldersExecutableDirectory"
		isNative = False
		class OpenFoldersExecutableDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersLocalizationDirectory:
		ID = "OpenFoldersLocalizationDirectory"
		isNative = False
		class OpenFoldersLocalizationDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersCoreAddInDirectory:
		ID = "OpenFoldersCoreAddInDirectory"
		isNative = False
		class OpenFoldersCoreAddInDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersStringTableDirectory:
		ID = "OpenFoldersStringTableDirectory"
		isNative = False
		class OpenFoldersStringTableDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAppDirectory:
		ID = "OpenFoldersAppDirectory"
		isNative = False
		class OpenFoldersAppDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersSharedExtensionDirectory:
		ID = "OpenFoldersSharedExtensionDirectory"
		isNative = False
		class OpenFoldersSharedExtensionDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersTemporaryDirectory:
		ID = "OpenFoldersTemporaryDirectory"
		isNative = False
		class OpenFoldersTemporaryDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersUnbrandedUserDataDirectory:
		ID = "OpenFoldersUnbrandedUserDataDirectory"
		isNative = False
		class OpenFoldersUnbrandedUserDataDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersUserDataDirectory:
		ID = "OpenFoldersUserDataDirectory"
		isNative = False
		class OpenFoldersUserDataDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAllUsersDataDirectory:
		ID = "OpenFoldersAllUsersDataDirectory"
		isNative = False
		class OpenFoldersAllUsersDataDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersUnbrandedUserAppPluginsDirectory:
		ID = "OpenFoldersUnbrandedUserAppPluginsDirectory"
		isNative = False
		class OpenFoldersUnbrandedUserAppPluginsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersBootstrapOptionDirectory:
		ID = "OpenFoldersBootstrapOptionDirectory"
		isNative = False
		class OpenFoldersBootstrapOptionDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersOptionsDirectory:
		ID = "OpenFoldersOptionsDirectory"
		isNative = False
		class OpenFoldersOptionsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersCloudCacheDirectory:
		ID = "OpenFoldersCloudCacheDirectory"
		isNative = False
		class OpenFoldersCloudCacheDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersScriptsDirectory:
		ID = "OpenFoldersScriptsDirectory"
		isNative = False
		class OpenFoldersScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAutorunScriptsDirectory:
		ID = "OpenFoldersAutorunScriptsDirectory"
		isNative = False
		class OpenFoldersAutorunScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersSamplesScriptsDirectory:
		ID = "OpenFoldersSamplesScriptsDirectory"
		isNative = False
		class OpenFoldersSamplesScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersProgramDataScriptsDirectory:
		ID = "OpenFoldersProgramDataScriptsDirectory"
		isNative = False
		class OpenFoldersProgramDataScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAppDataScriptsDirectory:
		ID = "OpenFoldersAppDataScriptsDirectory"
		isNative = False
		class OpenFoldersAppDataScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersManuallyInstalledScriptsDirectory:
		ID = "OpenFoldersManuallyInstalledScriptsDirectory"
		isNative = False
		class OpenFoldersManuallyInstalledScriptsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersMaterialsDirectory:
		ID = "OpenFoldersMaterialsDirectory"
		isNative = False
		class OpenFoldersMaterialsDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersTestTempDirectory:
		ID = "OpenFoldersTestTempDirectory"
		isNative = False
		class OpenFoldersTestTempDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersScratchDirectory:
		ID = "OpenFoldersScratchDirectory"
		isNative = False
		class OpenFoldersScratchDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersResultDirectory:
		ID = "OpenFoldersResultDirectory"
		isNative = False
		class OpenFoldersResultDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersSampleDirectory:
		ID = "OpenFoldersSampleDirectory"
		isNative = False
		class OpenFoldersSampleDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAppLogFilePath:
		ID = "OpenFoldersAppLogFilePath"
		isNative = False
		class OpenFoldersAppLogFilePath_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersCacheDirectory:
		ID = "OpenFoldersCacheDirectory"
		isNative = False
		class OpenFoldersCacheDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
	class OpenFoldersAutoSaveDirectory:
		ID = "OpenFoldersAutoSaveDirectory"
		isNative = False
		class OpenFoldersAutoSaveDirectory_control:
			isVisible = True
			isEnabled = True
			DefinitionType = "ButtonControlDefinition"
class AllPanels:
	class CAMJobPanel:
		ID = "CAMJobPanel"
		class IronSetup:
			ID = "IronSetup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronSetup = AllControls.IronSetup
		class IronNcProgram:
			ID = "IronNcProgram"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronNcProgram = AllControls.IronNcProgram
		class IronFolder:
			ID = "IronFolder"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			IronFolder = AllControls.IronFolder
		class IronPattern:
			ID = "IronPattern"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			IronPattern = AllControls.IronPattern
		class IronStrategy_manual:
			ID = "IronStrategy_manual"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_manual = AllControls.IronStrategy_manual
		class IronStrategy_probe:
			ID = "IronStrategy_probe"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_probe = AllControls.IronStrategy_probe
		class SeparatorAfter_IronStrategy_probe:
			ID = "SeparatorAfter_IronStrategy_probe"
			Index = 6
		class MSFWmdCreateAggregationAssetWorkingModelCmd:
			ID = "MSFWmdCreateAggregationAssetWorkingModelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			MSFWmdCreateAggregationAssetWorkingModelCmd = AllControls.MSFWmdCreateAggregationAssetWorkingModelCmd
	class CAMInProcessStockPanel:
		ID = "CAMInProcessStockPanel"
		class IronAutomaticIPSGeneration:
			ID = "IronAutomaticIPSGeneration"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronAutomaticIPSGeneration = AllControls.IronAutomaticIPSGeneration
	class CAMAdditiveJobPanel:
		ID = "CAMAdditiveJobPanel"
		class IronSetup:
			ID = "IronSetup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronSetup = AllControls.IronSetup
		class IronAdditiveImportGCode:
			ID = "IronAdditiveImportGCode"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			IronAdditiveImportGCode = AllControls.IronAdditiveImportGCode
		class SeparatorAfter_IronAdditiveImportGCode:
			ID = "SeparatorAfter_IronAdditiveImportGCode"
			Index = 2
		class MSFWmdCreateAggregationAssetWorkingModelCmd:
			ID = "MSFWmdCreateAggregationAssetWorkingModelCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			MSFWmdCreateAggregationAssetWorkingModelCmd = AllControls.MSFWmdCreateAggregationAssetWorkingModelCmd
	class CAMAdditivePositioningPanel:
		ID = "CAMAdditivePositioningPanel"
		class CAMMoveComponentsCommand:
			ID = "CAMMoveComponentsCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			CAMMoveComponentsCommand = AllControls.CAMMoveComponentsCommand
		class SeparatorAfter_CAMMoveComponentsCommand:
			ID = "SeparatorAfter_CAMMoveComponentsCommand"
			Index = 1
		class IronMinimizeBoundingBox:
			ID = "IronMinimizeBoundingBox"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronMinimizeBoundingBox = AllControls.IronMinimizeBoundingBox
		class IronStrategy_additive_optimize_orientation:
			ID = "IronStrategy_additive_optimize_orientation"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_additive_optimize_orientation = AllControls.IronStrategy_additive_optimize_orientation
		class SeparatorAfter_IronStrategy_additive_optimize_orientation:
			ID = "SeparatorAfter_IronStrategy_additive_optimize_orientation"
			Index = 4
		class IronPlaceOnPlatform:
			ID = "IronPlaceOnPlatform"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			IronPlaceOnPlatform = AllControls.IronPlaceOnPlatform
		class SeparatorAfter_IronPlaceOnPlatform:
			ID = "SeparatorAfter_IronPlaceOnPlatform"
			Index = 6
		class CollisionDetectionCmd:
			ID = "CollisionDetectionCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			CollisionDetectionCmd = AllControls.CollisionDetectionCmd
	class CAM2DPanel:
		ID = "CAM2DPanel"
		class IronStrategy_featureRecognition:
			ID = "IronStrategy_featureRecognition"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_featureRecognition = AllControls.IronStrategy_featureRecognition
		class IronStrategy_contourFeatureFolder:
			ID = "IronStrategy_contourFeatureFolder"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_contourFeatureFolder = AllControls.IronStrategy_contourFeatureFolder
		class IronStrategy_holeFeatureFolder:
			ID = "IronStrategy_holeFeatureFolder"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_holeFeatureFolder = AllControls.IronStrategy_holeFeatureFolder
		class SeparatorAfter_IronStrategy_holeFeatureFolder:
			ID = "SeparatorAfter_IronStrategy_holeFeatureFolder"
			Index = 3
		class IronStrategy_adaptive2d:
			ID = "IronStrategy_adaptive2d"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_adaptive2d = AllControls.IronStrategy_adaptive2d
		class IronStrategy_pocket2d:
			ID = "IronStrategy_pocket2d"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_pocket2d = AllControls.IronStrategy_pocket2d
		class SeparatorAfter_IronStrategy_pocket2d:
			ID = "SeparatorAfter_IronStrategy_pocket2d"
			Index = 6
		class IronStrategy_face:
			ID = "IronStrategy_face"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_face = AllControls.IronStrategy_face
		class IronStrategy_contour2d:
			ID = "IronStrategy_contour2d"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_contour2d = AllControls.IronStrategy_contour2d
		class IronStrategy_slot:
			ID = "IronStrategy_slot"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_slot = AllControls.IronStrategy_slot
		class IronStrategy_path3d:
			ID = "IronStrategy_path3d"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_path3d = AllControls.IronStrategy_path3d
		class SeparatorAfter_IronStrategy_path3d:
			ID = "SeparatorAfter_IronStrategy_path3d"
			Index = 11
		class IronStrategy_thread:
			ID = "IronStrategy_thread"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_thread = AllControls.IronStrategy_thread
		class IronStrategy_bore:
			ID = "IronStrategy_bore"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_bore = AllControls.IronStrategy_bore
		class IronStrategy_circular:
			ID = "IronStrategy_circular"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_circular = AllControls.IronStrategy_circular
		class IronStrategy_engrave:
			ID = "IronStrategy_engrave"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_engrave = AllControls.IronStrategy_engrave
		class IronStrategy_chamfer2d:
			ID = "IronStrategy_chamfer2d"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_chamfer2d = AllControls.IronStrategy_chamfer2d
	class CAM3DPanel:
		ID = "CAM3DPanel"
		class IronStrategy_adaptive:
			ID = "IronStrategy_adaptive"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_adaptive = AllControls.IronStrategy_adaptive
		class IronStrategy_pocket_new:
			ID = "IronStrategy_pocket_new"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_pocket_new = AllControls.IronStrategy_pocket_new
		class SeparatorAfter_IronStrategy_pocket_new:
			ID = "SeparatorAfter_IronStrategy_pocket_new"
			Index = 2
		class IronStrategy_steep_and_shallow:
			ID = "IronStrategy_steep_and_shallow"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_steep_and_shallow = AllControls.IronStrategy_steep_and_shallow
		class IronStrategy_flat:
			ID = "IronStrategy_flat"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_flat = AllControls.IronStrategy_flat
		class IronStrategy_parallel_new:
			ID = "IronStrategy_parallel_new"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_parallel_new = AllControls.IronStrategy_parallel_new
		class IronStrategy_scallop_new:
			ID = "IronStrategy_scallop_new"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_scallop_new = AllControls.IronStrategy_scallop_new
		class IronStrategy_contour_new:
			ID = "IronStrategy_contour_new"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_contour_new = AllControls.IronStrategy_contour_new
		class IronStrategy_ramp:
			ID = "IronStrategy_ramp"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_ramp = AllControls.IronStrategy_ramp
		class IronStrategy_pencil_new:
			ID = "IronStrategy_pencil_new"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_pencil_new = AllControls.IronStrategy_pencil_new
		class IronStrategy_horizontal_new:
			ID = "IronStrategy_horizontal_new"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_horizontal_new = AllControls.IronStrategy_horizontal_new
		class IronStrategy_spiral_new:
			ID = "IronStrategy_spiral_new"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_spiral_new = AllControls.IronStrategy_spiral_new
		class IronStrategy_radial_new:
			ID = "IronStrategy_radial_new"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_radial_new = AllControls.IronStrategy_radial_new
		class IronStrategy_morphed_spiral:
			ID = "IronStrategy_morphed_spiral"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_morphed_spiral = AllControls.IronStrategy_morphed_spiral
		class IronStrategy_project:
			ID = "IronStrategy_project"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_project = AllControls.IronStrategy_project
		class IronStrategy_blend:
			ID = "IronStrategy_blend"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_blend = AllControls.IronStrategy_blend
		class IronStrategy_morph:
			ID = "IronStrategy_morph"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_morph = AllControls.IronStrategy_morph
		class IronStrategy_rest_finishing:
			ID = "IronStrategy_rest_finishing"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_rest_finishing = AllControls.IronStrategy_rest_finishing
		class IronStrategy_flow:
			ID = "IronStrategy_flow"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_flow = AllControls.IronStrategy_flow
	class CAMEditPanel:
		ID = "CAMEditPanel"
		class IronToolpathTrim:
			ID = "IronToolpathTrim"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronToolpathTrim = AllControls.IronToolpathTrim
		class IronToolpathEditDelete:
			ID = "IronToolpathEditDelete"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronToolpathEditDelete = AllControls.IronToolpathEditDelete
		class IronToolpathEditLeadsLinks:
			ID = "IronToolpathEditLeadsLinks"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronToolpathEditLeadsLinks = AllControls.IronToolpathEditLeadsLinks
		class IronToolpathEditToolChange:
			ID = "IronToolpathEditToolChange"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronToolpathEditToolChange = AllControls.IronToolpathEditToolChange
		class IronToolpathEditMoveStartPoints:
			ID = "IronToolpathEditMoveStartPoints"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronToolpathEditMoveStartPoints = AllControls.IronToolpathEditMoveStartPoints
	class CAMDrillingPanel:
		ID = "CAMDrillingPanel"
		class IronStrategy_drill:
			ID = "IronStrategy_drill"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_drill = AllControls.IronStrategy_drill
		class IronHoleRecognition:
			ID = "IronHoleRecognition"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronHoleRecognition = AllControls.IronHoleRecognition
	class CAMMultiAxisPanel:
		ID = "CAMMultiAxisPanel"
		class IronStrategy_swarf5d:
			ID = "IronStrategy_swarf5d"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_swarf5d = AllControls.IronStrategy_swarf5d
		class IronStrategy_multiAxisContour:
			ID = "IronStrategy_multiAxisContour"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_multiAxisContour = AllControls.IronStrategy_multiAxisContour
		class IronStrategy_rotary_finishing:
			ID = "IronStrategy_rotary_finishing"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_rotary_finishing = AllControls.IronStrategy_rotary_finishing
	class CAMTurningPanel:
		ID = "CAMTurningPanel"
		class IronStrategy_turningFace:
			ID = "IronStrategy_turningFace"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningFace = AllControls.IronStrategy_turningFace
		class IronStrategy_turningProfileRoughing:
			ID = "IronStrategy_turningProfileRoughing"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningProfileRoughing = AllControls.IronStrategy_turningProfileRoughing
		class IronStrategy_turningProfileFinishing:
			ID = "IronStrategy_turningProfileFinishing"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningProfileFinishing = AllControls.IronStrategy_turningProfileFinishing
		class IronStrategy_turningRoughing:
			ID = "IronStrategy_turningRoughing"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningRoughing = AllControls.IronStrategy_turningRoughing
		class IronStrategy_turningAdaptiveRoughing:
			ID = "IronStrategy_turningAdaptiveRoughing"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningAdaptiveRoughing = AllControls.IronStrategy_turningAdaptiveRoughing
		class IronStrategy_turningProfileGroove:
			ID = "IronStrategy_turningProfileGroove"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningProfileGroove = AllControls.IronStrategy_turningProfileGroove
		class IronStrategy_turningGroove:
			ID = "IronStrategy_turningGroove"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningGroove = AllControls.IronStrategy_turningGroove
		class IronStrategy_turningThread:
			ID = "IronStrategy_turningThread"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningThread = AllControls.IronStrategy_turningThread
		class IronStrategy_turningChamfer:
			ID = "IronStrategy_turningChamfer"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningChamfer = AllControls.IronStrategy_turningChamfer
		class IronStrategy_turningPart:
			ID = "IronStrategy_turningPart"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_turningPart = AllControls.IronStrategy_turningPart
		class IronStrategy_turningSecondarySpindleGrab:
			ID = "IronStrategy_turningSecondarySpindleGrab"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningSecondarySpindleGrab = AllControls.IronStrategy_turningSecondarySpindleGrab
		class IronStrategy_turningSecondarySpindlePull:
			ID = "IronStrategy_turningSecondarySpindlePull"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningSecondarySpindlePull = AllControls.IronStrategy_turningSecondarySpindlePull
		class IronStrategy_turningSecondarySpindleReturn:
			ID = "IronStrategy_turningSecondarySpindleReturn"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_turningSecondarySpindleReturn = AllControls.IronStrategy_turningSecondarySpindleReturn
	class CAMWLPCPanel:
		ID = "CAMWLPCPanel"
		class IronStrategy_jet2d:
			ID = "IronStrategy_jet2d"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_jet2d = AllControls.IronStrategy_jet2d
	class CAMInfillPanel:
		ID = "CAMInfillPanel"
		class IronFFFInfillCmd:
			ID = "IronFFFInfillCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronFFFInfillCmd = AllControls.IronFFFInfillCmd
	class CAMSupportsPanel:
		ID = "CAMSupportsPanel"
		class IronFFFSupportsCmd:
			ID = "IronFFFSupportsCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronFFFSupportsCmd = AllControls.IronFFFSupportsCmd
		class IronStrategy_areavolume_additive_support:
			ID = "IronStrategy_areavolume_additive_support"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_areavolume_additive_support = AllControls.IronStrategy_areavolume_additive_support
		class IronStrategy_surroundvolumepolyline_additive_support:
			ID = "IronStrategy_surroundvolumepolyline_additive_support"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_surroundvolumepolyline_additive_support = AllControls.IronStrategy_surroundvolumepolyline_additive_support
		class SeparatorAfter_IronStrategy_surroundvolumepolyline_additive_support:
			ID = "SeparatorAfter_IronStrategy_surroundvolumepolyline_additive_support"
			Index = 3
		class IronStrategy_areabar_additive_support:
			ID = "IronStrategy_areabar_additive_support"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_areabar_additive_support = AllControls.IronStrategy_areabar_additive_support
		class IronStrategy_downoriented_additive_support:
			ID = "IronStrategy_downoriented_additive_support"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_downoriented_additive_support = AllControls.IronStrategy_downoriented_additive_support
		class IronStrategy_lattice_additive_support:
			ID = "IronStrategy_lattice_additive_support"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_lattice_additive_support = AllControls.IronStrategy_lattice_additive_support
		class SeparatorAfter_IronStrategy_lattice_additive_support:
			ID = "SeparatorAfter_IronStrategy_lattice_additive_support"
			Index = 7
		class IronStrategy_areapolyline_additive_support:
			ID = "IronStrategy_areapolyline_additive_support"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_areapolyline_additive_support = AllControls.IronStrategy_areapolyline_additive_support
		class IronStrategy_edgepolyline_additive_support:
			ID = "IronStrategy_edgepolyline_additive_support"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_edgepolyline_additive_support = AllControls.IronStrategy_edgepolyline_additive_support
		class IronStrategy_clustercontourpolyline_additive_support:
			ID = "IronStrategy_clustercontourpolyline_additive_support"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_clustercontourpolyline_additive_support = AllControls.IronStrategy_clustercontourpolyline_additive_support
		class IronStrategy_skeletonpolyline_additive_support:
			ID = "IronStrategy_skeletonpolyline_additive_support"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_skeletonpolyline_additive_support = AllControls.IronStrategy_skeletonpolyline_additive_support
		class SeparatorAfter_IronStrategy_skeletonpolyline_additive_support:
			ID = "SeparatorAfter_IronStrategy_skeletonpolyline_additive_support"
			Index = 12
		class IronStrategy_baseplate_additive_support:
			ID = "IronStrategy_baseplate_additive_support"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_baseplate_additive_support = AllControls.IronStrategy_baseplate_additive_support
	class CAMDEDPanel:
		ID = "CAMDEDPanel"
		class IronStrategy_feature_construction:
			ID = "IronStrategy_feature_construction"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_feature_construction = AllControls.IronStrategy_feature_construction
	class CAMAdditiveProcessSimPanel:
		ID = "CAMAdditiveProcessSimPanel"
		class IronAdditiveProcessSimulation:
			ID = "IronAdditiveProcessSimulation"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimulation = AllControls.IronAdditiveProcessSimulation
		class IronAdditiveProcessSimMesh:
			ID = "IronAdditiveProcessSimMesh"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimMesh = AllControls.IronAdditiveProcessSimMesh
		class IronAdditiveProcessSimPreCheck:
			ID = "IronAdditiveProcessSimPreCheck"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimPreCheck = AllControls.IronAdditiveProcessSimPreCheck
		class IronAdditiveProcessSimSolve:
			ID = "IronAdditiveProcessSimSolve"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimSolve = AllControls.IronAdditiveProcessSimSolve
		class SeparatorAfter_IronAdditiveProcessSimSolve:
			ID = "SeparatorAfter_IronAdditiveProcessSimSolve"
			Index = 4
		class IronAdditiveMeshView:
			ID = "IronAdditiveMeshView"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			IronAdditiveMeshView = AllControls.IronAdditiveMeshView
		class IronAdditiveResultsView:
			ID = "IronAdditiveResultsView"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronAdditiveResultsView = AllControls.IronAdditiveResultsView
	class CAMAdditiveProcessSimResultsPanel:
		ID = "CAMAdditiveProcessSimResultsPanel"
		class IronAdditiveProcessSimToggleEdges:
			ID = "IronAdditiveProcessSimToggleEdges"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimToggleEdges = AllControls.IronAdditiveProcessSimToggleEdges
		class IronAdditiveProcessSimMinMaxProbe:
			ID = "IronAdditiveProcessSimMinMaxProbe"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimMinMaxProbe = AllControls.IronAdditiveProcessSimMinMaxProbe
		class IronAdditiveOpenResultsFolder:
			ID = "IronAdditiveOpenResultsFolder"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveOpenResultsFolder = AllControls.IronAdditiveOpenResultsFolder
		class IronAdditiveProcessSimSolve:
			ID = "IronAdditiveProcessSimSolve"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveProcessSimSolve = AllControls.IronAdditiveProcessSimSolve
		class IronAdditiveExportCompensated:
			ID = "IronAdditiveExportCompensated"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveExportCompensated = AllControls.IronAdditiveExportCompensated
	class CAMAdditiveProcessSimActionPanel:
		ID = "CAMAdditiveProcessSimActionPanel"
		class IronAdditiveExportCompensatedSTL:
			ID = "IronAdditiveExportCompensatedSTL"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveExportCompensatedSTL = AllControls.IronAdditiveExportCompensatedSTL
	class CAMAdditiveProcessSimFinishPanel:
		ID = "CAMAdditiveProcessSimFinishPanel"
		class AdditiveResultsStop:
			ID = "AdditiveResultsStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			AdditiveResultsStop = AllControls.AdditiveResultsStop
	class CAMProbingPanel:
		ID = "CAMProbingPanel"
		class IronStrategy_probe:
			ID = "IronStrategy_probe"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_probe = AllControls.IronStrategy_probe
		class IronStrategy_probe_geometry:
			ID = "IronStrategy_probe_geometry"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_probe_geometry = AllControls.IronStrategy_probe_geometry
		class IronStrategy_inspectSurface:
			ID = "IronStrategy_inspectSurface"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_inspectSurface = AllControls.IronStrategy_inspectSurface
		class PartAlignmentStart_Delayed:
			ID = "PartAlignmentStart_Delayed"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			PartAlignmentStart_Delayed = AllControls.PartAlignmentStart_Delayed
		class PartAlignmentStart_Live:
			ID = "PartAlignmentStart_Live"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			PartAlignmentStart_Live = AllControls.PartAlignmentStart_Live
	class CAMCMMPanel:
		ID = "CAMCMMPanel"
		class IronStrategy_cmm_inspection_setup:
			ID = "IronStrategy_cmm_inspection_setup"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_cmm_inspection_setup = AllControls.IronStrategy_cmm_inspection_setup
		class IronStrategy_datum:
			ID = "IronStrategy_datum"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_datum = AllControls.IronStrategy_datum
		class MeasureSurface:
			ID = "MeasureSurface"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			MeasureSurface = AllControls.MeasureSurface
		class ScanSurface:
			ID = "ScanSurface"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ScanSurface = AllControls.ScanSurface
	class CAMManualInspectionPanel:
		ID = "CAMManualInspectionPanel"
		class IronCreateInspections:
			ID = "IronCreateInspections"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronCreateInspections = AllControls.IronCreateInspections
		class IronRecordManualMeasure:
			ID = "IronRecordManualMeasure"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronRecordManualMeasure = AllControls.IronRecordManualMeasure
	class CAMPartAlignmentEditPanel:
		ID = "CAMPartAlignmentEditPanel"
		class PartAlignment_EditAlignment:
			ID = "PartAlignment_EditAlignment"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_EditAlignment = AllControls.PartAlignment_EditAlignment
	class CAMPartAlignmentInspectPanel:
		ID = "CAMPartAlignmentInspectPanel"
		class PartAlignment_IronStrategy_inspectSurface:
			ID = "PartAlignment_IronStrategy_inspectSurface"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronStrategy_inspectSurface = AllControls.PartAlignment_IronStrategy_inspectSurface
	class CAMPartAlignmentPostPanel:
		ID = "CAMPartAlignmentPostPanel"
		class PartAlignment_IronNcProgram:
			ID = "PartAlignment_IronNcProgram"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronNcProgram = AllControls.PartAlignment_IronNcProgram
	class CAMLiveAlignmentPostPanel:
		ID = "CAMLiveAlignmentPostPanel"
		class PartAlignmentPostLive:
			ID = "PartAlignmentPostLive"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignmentPostLive = AllControls.PartAlignmentPostLive
	class CAMPartAlignmentResultsPanel:
		ID = "CAMPartAlignmentResultsPanel"
		class PartAlignment_ImportResults:
			ID = "PartAlignment_ImportResults"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_ImportResults = AllControls.PartAlignment_ImportResults
		class PartAlignment_IronPartAlignmentInfo:
			ID = "PartAlignment_IronPartAlignmentInfo"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronPartAlignmentInfo = AllControls.PartAlignment_IronPartAlignmentInfo
		class PartAlignment_IronShowResults:
			ID = "PartAlignment_IronShowResults"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronShowResults = AllControls.PartAlignment_IronShowResults
	class CAMLiveAlignmentResultsPanel:
		ID = "CAMLiveAlignmentResultsPanel"
		class LivePartAlignment:
			ID = "LivePartAlignment"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			LivePartAlignment = AllControls.LivePartAlignment
		class PartAlignment_IronPartAlignmentInfo:
			ID = "PartAlignment_IronPartAlignmentInfo"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronPartAlignmentInfo = AllControls.PartAlignment_IronPartAlignmentInfo
		class PartAlignment_IronShowResults:
			ID = "PartAlignment_IronShowResults"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PartAlignment_IronShowResults = AllControls.PartAlignment_IronShowResults
	class CAMPartAlignmentPostAndExitPanel:
		ID = "CAMPartAlignmentPostAndExitPanel"
		class PartAlignmentPostStop:
			ID = "PartAlignmentPostStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignmentPostStop = AllControls.PartAlignmentPostStop
	class CAMPartAlignmentFinishPanel:
		ID = "CAMPartAlignmentFinishPanel"
		class PartAlignmentStop_Delayed:
			ID = "PartAlignmentStop_Delayed"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignmentStop_Delayed = AllControls.PartAlignmentStop_Delayed
	class CAMLiveAlignmentFinishPanel:
		ID = "CAMLiveAlignmentFinishPanel"
		class PartAlignmentStop_Live:
			ID = "PartAlignmentStop_Live"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PartAlignmentStop_Live = AllControls.PartAlignmentStop_Live
	class CAMActionPanel:
		ID = "CAMActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			IronGenerateToolpath = AllControls.IronGenerateToolpath
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronSimulation = AllControls.IronSimulation
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronPostProcess = AllControls.IronPostProcess
		class IronSetupSheetSwitchboard:
			ID = "IronSetupSheetSwitchboard"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronSetupSheetSwitchboard = AllControls.IronSetupSheetSwitchboard
	class CAMProbingActionPanel:
		ID = "CAMProbingActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			IronGenerateToolpath = AllControls.IronGenerateToolpath
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronSimulation = AllControls.IronSimulation
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronPostProcess = AllControls.IronPostProcess
		class IronSetupSheetSwitchboard:
			ID = "IronSetupSheetSwitchboard"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronSetupSheetSwitchboard = AllControls.IronSetupSheetSwitchboard
		class ImportResults:
			ID = "ImportResults"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			ImportResults = AllControls.ImportResults
		class LiveProbing:
			ID = "LiveProbing"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			LiveProbing = AllControls.LiveProbing
		class IronInspectionReport:
			ID = "IronInspectionReport"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronInspectionReport = AllControls.IronInspectionReport
	class CAMAdditivePrintProfilePanel:
		ID = "CAMAdditivePrintProfilePanel"
		class SimplePrintSettingSelection:
			ID = "SimplePrintSettingSelection"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SimplePrintSettingSelection = AllControls.SimplePrintSettingSelection
		class IronAdditiveEditPrintSetting:
			ID = "IronAdditiveEditPrintSetting"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveEditPrintSetting = AllControls.IronAdditiveEditPrintSetting
		class IronAdditiveBuildStrategy:
			ID = "IronAdditiveBuildStrategy"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveBuildStrategy = AllControls.IronAdditiveBuildStrategy
	class CAMAdditiveActionPanel:
		ID = "CAMAdditiveActionPanel"
		class IronGenerateToolpath:
			ID = "IronGenerateToolpath"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronGenerateToolpath = AllControls.IronGenerateToolpath
		class IronSimulation:
			ID = "IronSimulation"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronSimulation = AllControls.IronSimulation
		class IronAdditiveSimulation:
			ID = "IronAdditiveSimulation"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveSimulation = AllControls.IronAdditiveSimulation
		class IronPostProcess:
			ID = "IronPostProcess"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronPostProcess = AllControls.IronPostProcess
		class IronAdditiveExportStrategy:
			ID = "IronAdditiveExportStrategy"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronAdditiveExportStrategy = AllControls.IronAdditiveExportStrategy
		class SeparatorAfter_IronAdditiveExportStrategy:
			ID = "SeparatorAfter_IronAdditiveExportStrategy"
			Index = 5
		class IronAdditiveShowPrintStatistics:
			ID = "IronAdditiveShowPrintStatistics"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronAdditiveShowPrintStatistics = AllControls.IronAdditiveShowPrintStatistics
		class Iron3MFExport:
			ID = "Iron3MFExport"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			Iron3MFExport = AllControls.Iron3MFExport
		class IronFormlabsExport:
			ID = "IronFormlabsExport"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			IronFormlabsExport = AllControls.IronFormlabsExport
	class CAMInspectPanel:
		ID = "CAMInspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			InterferenceCheckCommand = AllControls.InterferenceCheckCommand
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionAccessibilityAnalysisCommand = AllControls.FusionAccessibilityAnalysisCommand
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionMinimumRadiusAnalysisCommand = AllControls.FusionMinimumRadiusAnalysisCommand
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionHalfSectionViewCommand = AllControls.FusionHalfSectionViewCommand
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionZebraAnalysisCommand = AllControls.FusionZebraAnalysisCommand
	class CAMManagePanel:
		ID = "CAMManagePanel"
		class IronStrategy_create_form_mill:
			ID = "IronStrategy_create_form_mill"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_create_form_mill = AllControls.IronStrategy_create_form_mill
		class IronToolLibrary:
			ID = "IronToolLibrary"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronToolLibrary = AllControls.IronToolLibrary
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronMachineLibrary = AllControls.IronMachineLibrary
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronPostLibrary = AllControls.IronPostLibrary
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronTemplateLibrary = AllControls.IronTemplateLibrary
		class IronSetupSheetConfigurations:
			ID = "IronSetupSheetConfigurations"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			IronSetupSheetConfigurations = AllControls.IronSetupSheetConfigurations
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronTaskManager = AllControls.IronTaskManager
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 7
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			IronExportDefaults = AllControls.IronExportDefaults
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			IronImportDefaults = AllControls.IronImportDefaults
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronResetDefaults = AllControls.IronResetDefaults
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 11
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			IronTranslation = AllControls.IronTranslation
	class CAMAdditiveManagePanel:
		ID = "CAMAdditiveManagePanel"
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronMachineLibrary = AllControls.IronMachineLibrary
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronPostLibrary = AllControls.IronPostLibrary
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronTemplateLibrary = AllControls.IronTemplateLibrary
		class IronPrintSettingLibrary:
			ID = "IronPrintSettingLibrary"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronPrintSettingLibrary = AllControls.IronPrintSettingLibrary
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			IronTaskManager = AllControls.IronTaskManager
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 5
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			IronExportDefaults = AllControls.IronExportDefaults
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			IronImportDefaults = AllControls.IronImportDefaults
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			IronResetDefaults = AllControls.IronResetDefaults
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 9
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			IronTranslation = AllControls.IronTranslation
	class CAMGeometryFeatures:
		ID = "CAMGeometryFeatures"
		class IronStrategy_geometry_contours:
			ID = "IronStrategy_geometry_contours"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_geometry_contours = AllControls.IronStrategy_geometry_contours
		class IronStrategy_geometry_pockets:
			ID = "IronStrategy_geometry_pockets"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_geometry_pockets = AllControls.IronStrategy_geometry_pockets
		class IronStrategy_pocket_recognition:
			ID = "IronStrategy_pocket_recognition"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_pocket_recognition = AllControls.IronStrategy_pocket_recognition
		class IronStrategy_geometry_silhouette:
			ID = "IronStrategy_geometry_silhouette"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			IronStrategy_geometry_silhouette = AllControls.IronStrategy_geometry_silhouette
	class CAMScriptsAddinsPanel:
		ID = "CAMScriptsAddinsPanel"
		class ScriptsManagerCommand:
			ID = "ScriptsManagerCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ScriptsManagerCommand = AllControls.ScriptsManagerCommand
		class ExchangeAppStoreCommand:
			ID = "ExchangeAppStoreCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			ExchangeAppStoreCommand = AllControls.ExchangeAppStoreCommand
	class SelectPanel:
		ID = "SelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SelectCommand = AllControls.SelectCommand
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			selectWindow = AllControls.selectWindow
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			selectFreeForm = AllControls.selectFreeForm
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			selectPaint = AllControls.selectPaint
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SelectionPriorityCommands:
			ID = "SelectionPriorityCommands"
			Index = 6
			class SelectBodyPriorityCommand:
				ID = "SelectBodyPriorityCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				SelectBodyPriorityCommand = AllControls.SelectBodyPriorityCommand
			class SelectFacePriorityCommand:
				ID = "SelectFacePriorityCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				SelectFacePriorityCommand = AllControls.SelectFacePriorityCommand
			class SelectEdgePriorityCommand:
				ID = "SelectEdgePriorityCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				SelectEdgePriorityCommand = AllControls.SelectEdgePriorityCommand
			class SelectComponentPriorityCommand:
				ID = "SelectComponentPriorityCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
				SelectComponentPriorityCommand = AllControls.SelectComponentPriorityCommand
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			SelectionFilterCommand = AllControls.SelectionFilterCommand
	class ManufacturingSourcesPanel:
		ID = "ManufacturingSourcesPanel"
		class MSFWmdComponentLibraryCmd:
			ID = "MSFWmdComponentLibraryCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MSFWmdComponentLibraryCmd = AllControls.MSFWmdComponentLibraryCmd
	class FabricationManagePanel:
		ID = "FabricationManagePanel"
		class MSF_MAGMatLibraryCmd_FusionNesting:
			ID = "MSF.MAGMatLibraryCmd.FusionNesting"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
			MSF_MAGMatLibraryCmd_FusionNesting = AllControls.MSF_MAGMatLibraryCmd_FusionNesting
		class MSF_MSFNestSaveContainerDataCmd_Create:
			ID = "MSF.MSFNestSaveContainerDataCmd.Create"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
			MSF_MSFNestSaveContainerDataCmd_Create = AllControls.MSF_MSFNestSaveContainerDataCmd_Create
		class Nesting_Separator:
			ID = "Nesting.Separator"
			Index = 2
		class MSFNestNameConventionCmd:
			ID = "MSFNestNameConventionCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = False
			MSFNestNameConventionCmd = AllControls.MSFNestNameConventionCmd
		class IronStrategy_create_form_mill:
			ID = "IronStrategy_create_form_mill"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			IronStrategy_create_form_mill = AllControls.IronStrategy_create_form_mill
		class IronToolLibrary:
			ID = "IronToolLibrary"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			IronToolLibrary = AllControls.IronToolLibrary
		class IronMachineLibrary:
			ID = "IronMachineLibrary"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			IronMachineLibrary = AllControls.IronMachineLibrary
		class IronPostLibrary:
			ID = "IronPostLibrary"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
			IronPostLibrary = AllControls.IronPostLibrary
		class IronTemplateLibrary:
			ID = "IronTemplateLibrary"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			IronTemplateLibrary = AllControls.IronTemplateLibrary
		class IronSetupSheetConfigurations:
			ID = "IronSetupSheetConfigurations"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			IronSetupSheetConfigurations = AllControls.IronSetupSheetConfigurations
		class IronTaskManager:
			ID = "IronTaskManager"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			IronTaskManager = AllControls.IronTaskManager
		class SeparatorAfter_IronTaskManager:
			ID = "SeparatorAfter_IronTaskManager"
			Index = 11
		class IronExportDefaults:
			ID = "IronExportDefaults"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			IronExportDefaults = AllControls.IronExportDefaults
		class IronImportDefaults:
			ID = "IronImportDefaults"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			IronImportDefaults = AllControls.IronImportDefaults
		class IronResetDefaults:
			ID = "IronResetDefaults"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			IronResetDefaults = AllControls.IronResetDefaults
		class SeparatorAfter_IronResetDefaults:
			ID = "SeparatorAfter_IronResetDefaults"
			Index = 15
		class IronShowTemplateSelector:
			ID = "IronShowTemplateSelector"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
		class IronTranslation:
			ID = "IronTranslation"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			IronTranslation = AllControls.IronTranslation
	class MachineBuilderActivationPanel:
		ID = "MachineBuilderActivationPanel"
		class MachineBuilderStart:
			ID = "MachineBuilder::Start"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MachineBuilderStart = AllControls.MachineBuilderStart
	class NESTPanel:
		ID = "NESTPanel"
		class MSFNestPrepareNestCmd:
			ID = "MSFNestPrepareNestCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
			MSFNestPrepareNestCmd = AllControls.MSFNestPrepareNestCmd
		class MSF_MAGNestCalculateCmd_Generate:
			ID = "MSF.MAGNestCalculateCmd.Generate"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			MSF_MAGNestCalculateCmd_Generate = AllControls.MSF_MAGNestCalculateCmd_Generate
	class StoryboardPanel:
		ID = "3DStoryboardPanel"
		class PublisherCreateStoryboardCommand:
			ID = "PublisherCreateStoryboardCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PublisherCreateStoryboardCommand = AllControls.PublisherCreateStoryboardCommand
	class ComponentPanel:
		ID = "3DComponentPanel"
		class PublisherMoveComponentsCommand:
			ID = "PublisherMoveComponentsCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PublisherMoveComponentsCommand = AllControls.PublisherMoveComponentsCommand
		class PublisherRestoreHomeCommand:
			ID = "PublisherRestoreHomeCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			PublisherRestoreHomeCommand = AllControls.PublisherRestoreHomeCommand
		class PublisherExplodeDirectChildrenCommand:
			ID = "PublisherExplodeDirectChildrenCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			PublisherExplodeDirectChildrenCommand = AllControls.PublisherExplodeDirectChildrenCommand
		class PublisherExplodeAllPartsCommand:
			ID = "PublisherExplodeAllPartsCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			PublisherExplodeAllPartsCommand = AllControls.PublisherExplodeAllPartsCommand
		class PublisherManualExplodeCommand:
			ID = "PublisherManualExplodeCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			PublisherManualExplodeCommand = AllControls.PublisherManualExplodeCommand
		class PublisherVisibilityToggleCmd:
			ID = "PublisherVisibilityToggleCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			PublisherVisibilityToggleCmd = AllControls.PublisherVisibilityToggleCmd
		class PublisherAppearanceCommand:
			ID = "PublisherAppearanceCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			PublisherAppearanceCommand = AllControls.PublisherAppearanceCommand
	class AnnotationPanel:
		ID = "AnnotationPanel"
		class CalloutCommand:
			ID = "CalloutCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class PublisherViewPanel:
		ID = "PublisherViewPanel"
		class PublisherToggleCameraRecordingCmd:
			ID = "PublisherToggleCameraRecordingCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PublisherToggleCameraRecordingCmd = AllControls.PublisherToggleCameraRecordingCmd
	class PublishVideoPanel:
		ID = "PublishVideoPanel"
		class ExportVideoCommand:
			ID = "ExportVideoCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ExportVideoCommand = AllControls.ExportVideoCommand
	class FilePanel:
		ID = "FilePanel"
		class NewSingleDocumentCommand:
			ID = "NewSingleDocumentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			NewSingleDocumentCommand = AllControls.NewSingleDocumentCommand
		class NewDocumentCommand:
			ID = "NewDocumentCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			NewDocumentCommand = AllControls.NewDocumentCommand
		class SaveDocumentAsCommand:
			ID = "SaveDocumentAsCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			SaveDocumentAsCommand = AllControls.SaveDocumentAsCommand
	class DiagnosticsPanel:
		ID = "DiagnosticsPanel"
		class HideTextCommandsCommand:
			ID = "HideTextCommandsCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			HideTextCommandsCommand = AllControls.HideTextCommandsCommand
		class ShowTextCommandsCommand:
			ID = "ShowTextCommandsCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			ShowTextCommandsCommand = AllControls.ShowTextCommandsCommand
		class HideDebugDialogCommand:
			ID = "HideDebugDialogCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			HideDebugDialogCommand = AllControls.HideDebugDialogCommand
		class ShowDebugDialogCommand:
			ID = "ShowDebugDialogCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ShowDebugDialogCommand = AllControls.ShowDebugDialogCommand
		class NTestImportCommand:
			ID = "NTestImportCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class DiagnosticsCommand:
			ID = "DiagnosticsCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			DiagnosticsCommand = AllControls.DiagnosticsCommand
		class DataBrowserCommand:
			ID = "DataBrowserCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			DataBrowserCommand = AllControls.DataBrowserCommand
		class DumpEntityCommand:
			ID = "DumpEntityCommand"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
			DumpEntityCommand = AllControls.DumpEntityCommand
		class EntityFinderCommand:
			ID = "EntityFinderCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			EntityFinderCommand = AllControls.EntityFinderCommand
		class TSplineDumpEntityCommand:
			ID = "TSplineDumpEntityCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
			TSplineDumpEntityCommand = AllControls.TSplineDumpEntityCommand
		class TSplineSaveAsTSMCommand:
			ID = "TSplineSaveAsTSMCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
			TSplineSaveAsTSMCommand = AllControls.TSplineSaveAsTSMCommand
		class TSplineDiagnosticCommand:
			ID = "TSplineDiagnosticCommand"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
			TSplineDiagnosticCommand = AllControls.TSplineDiagnosticCommand
		class AssemblyInfoCommand:
			ID = "AssemblyInfoCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			AssemblyInfoCommand = AllControls.AssemblyInfoCommand
		class SanityCheckCommand:
			ID = "SanityCheckCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			SanityCheckCommand = AllControls.SanityCheckCommand
		class ASMDebugOptionsCommand:
			ID = "ASMDebugOptionsCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			ASMDebugOptionsCommand = AllControls.ASMDebugOptionsCommand
		class ASMDebugChecksCommand:
			ID = "ASMDebugChecksCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			ASMDebugChecksCommand = AllControls.ASMDebugChecksCommand
		class RunTestsCommand:
			ID = "RunTestsCommand"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
			RunTestsCommand = AllControls.RunTestsCommand
		class CollaborationMockDebugCmd:
			ID = "CollaborationMockDebugCmd"
			Index = 17
			isPromoted = True
			isPromotedByDefault = True
			CollaborationMockDebugCmd = AllControls.CollaborationMockDebugCmd
		class SketchAutoConstrainCmd:
			ID = "SketchAutoConstrainCmd"
			Index = 18
			isPromoted = True
			isPromotedByDefault = True
			SketchAutoConstrainCmd = AllControls.SketchAutoConstrainCmd
	class UIDemo:
		ID = "UIDemo"
		class TestTableCommand:
			ID = "TestTableCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			TestTableCommand = AllControls.TestTableCommand
		class TestTabBarCommand:
			ID = "TestTabBarCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			TestTabBarCommand = AllControls.TestTabBarCommand
		class TestToolkitCommand:
			ID = "TestToolkitCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			TestToolkitCommand = AllControls.TestToolkitCommand
		class TestOptionGroupCommand:
			ID = "TestOptionGroupCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			TestOptionGroupCommand = AllControls.TestOptionGroupCommand
		class TestPropertyDialogCommand:
			ID = "TestPropertyDialogCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
		class DemoControlsCommand:
			ID = "DemoControlsCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
		class DemoControls2Command:
			ID = "DemoControls2Command"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			DemoControls2Command = AllControls.DemoControls2Command
	class SketchCreatePanel:
		ID = "SketchCreatePanel"
		class DrawPolyline:
			ID = "DrawPolyline"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			DrawPolyline = AllControls.DrawPolyline
		class RectangleDropDown:
			ID = "RectangleDropDown"
			Index = 1
			class ShapeRectangleTwoPoint:
				ID = "ShapeRectangleTwoPoint"
				Index = 0
				ShapeRectangleTwoPoint = AllControls.ShapeRectangleTwoPoint
			class ShapeRectangleThreePoint:
				ID = "ShapeRectangleThreePoint"
				Index = 1
				ShapeRectangleThreePoint = AllControls.ShapeRectangleThreePoint
			class ShapeRectangleCenter:
				ID = "ShapeRectangleCenter"
				Index = 2
				ShapeRectangleCenter = AllControls.ShapeRectangleCenter
		class CircleDropDown:
			ID = "CircleDropDown"
			Index = 2
			class CircleCenterRadius:
				ID = "CircleCenterRadius"
				Index = 0
				CircleCenterRadius = AllControls.CircleCenterRadius
			class CircleTwoPoint:
				ID = "CircleTwoPoint"
				Index = 1
				CircleTwoPoint = AllControls.CircleTwoPoint
			class CircleThreePoint:
				ID = "CircleThreePoint"
				Index = 2
				CircleThreePoint = AllControls.CircleThreePoint
			class CircleTanTanRadius:
				ID = "CircleTanTanRadius"
				Index = 3
				CircleTanTanRadius = AllControls.CircleTanTanRadius
			class CircleThreeTangent:
				ID = "CircleThreeTangent"
				Index = 4
				CircleThreeTangent = AllControls.CircleThreeTangent
		class ArcDropDown:
			ID = "ArcDropDown"
			Index = 3
			class ArcThreePoint:
				ID = "ArcThreePoint"
				Index = 0
				ArcThreePoint = AllControls.ArcThreePoint
			class ArcCenterTwoPoint:
				ID = "ArcCenterTwoPoint"
				Index = 1
				ArcCenterTwoPoint = AllControls.ArcCenterTwoPoint
			class ArcTangent:
				ID = "ArcTangent"
				Index = 2
				ArcTangent = AllControls.ArcTangent
		class PolygonDropDown:
			ID = "PolygonDropDown"
			Index = 4
			class ShapePolygonCircumscribed:
				ID = "ShapePolygonCircumscribed"
				Index = 0
				ShapePolygonCircumscribed = AllControls.ShapePolygonCircumscribed
			class ShapePolygonInscribed:
				ID = "ShapePolygonInscribed"
				Index = 1
				ShapePolygonInscribed = AllControls.ShapePolygonInscribed
			class ShapePolygonEdge:
				ID = "ShapePolygonEdge"
				Index = 2
				ShapePolygonEdge = AllControls.ShapePolygonEdge
		class CircleElipse:
			ID = "CircleElipse"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			CircleElipse = AllControls.CircleElipse
		class SlotDropDown:
			ID = "SlotDropDown"
			Index = 6
			class ShapeSlotCenterToCenter:
				ID = "ShapeSlotCenterToCenter"
				Index = 0
				ShapeSlotCenterToCenter = AllControls.ShapeSlotCenterToCenter
			class ShapeSlotOverall:
				ID = "ShapeSlotOverall"
				Index = 1
				ShapeSlotOverall = AllControls.ShapeSlotOverall
			class ShapeSlotCenterPoint:
				ID = "ShapeSlotCenterPoint"
				Index = 2
				ShapeSlotCenterPoint = AllControls.ShapeSlotCenterPoint
			class ShapeArcSlotThreePoint:
				ID = "ShapeArcSlotThreePoint"
				Index = 3
				ShapeArcSlotThreePoint = AllControls.ShapeArcSlotThreePoint
			class ShapeArcSlotCenterTwoPoint:
				ID = "ShapeArcSlotCenterTwoPoint"
				Index = 4
				ShapeArcSlotCenterTwoPoint = AllControls.ShapeArcSlotCenterTwoPoint
		class SplineDropDown:
			ID = "SplineDropDown"
			Index = 7
			class DrawSpline:
				ID = "DrawSpline"
				Index = 0
				DrawSpline = AllControls.DrawSpline
			class DrawCVMSpline3D:
				ID = "DrawCVMSpline3D"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				DrawCVMSpline3D = AllControls.DrawCVMSpline3D
			class DrawCVMSpline5D:
				ID = "DrawCVMSpline5D"
				Index = 2
				DrawCVMSpline5D = AllControls.DrawCVMSpline5D
		class ConicCurveCmd:
			ID = "ConicCurveCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			ConicCurveCmd = AllControls.ConicCurveCmd
		class DrawPoint:
			ID = "DrawPoint"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			DrawPoint = AllControls.DrawPoint
		class TextCmd:
			ID = "TextCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			TextCmd = AllControls.TextCmd
		class MTextCmd:
			ID = "MTextCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			MTextCmd = AllControls.MTextCmd
		class SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_MTextCmd"
			Index = 12
		class FitCurvesToSectionCommand:
			ID = "FitCurvesToSectionCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			FitCurvesToSectionCommand = AllControls.FitCurvesToSectionCommand
		class SeparatorAfter_FitCurvesToSectionCommand:
			ID = "SeparatorAfter_FitCurvesToSectionCommand"
			Index = 14
		class MirrorSketchCommand:
			ID = "MirrorSketchCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
			MirrorSketchCommand = AllControls.MirrorSketchCommand
		class CircularSketchPatternCommand:
			ID = "CircularSketchPatternCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			CircularSketchPatternCommand = AllControls.CircularSketchPatternCommand
		class RectangularSketchPatternCommand:
			ID = "RectangularSketchPatternCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			RectangularSketchPatternCommand = AllControls.RectangularSketchPatternCommand
		class SeparatorAfter_RectangularSketchPatternCommand:
			ID = "SeparatorAfter_RectangularSketchPatternCommand"
			Index = 18
		class ProjectIncludeDropDown:
			ID = "ProjectIncludeDropDown"
			Index = 19
			class ProjectNewCmd:
				ID = "ProjectNewCmd"
				Index = 0
				ProjectNewCmd = AllControls.ProjectNewCmd
			class IntersectCmd:
				ID = "IntersectCmd"
				Index = 1
				IntersectCmd = AllControls.IntersectCmd
			class SeparatorAfter_IntersectCmd:
				ID = "SeparatorAfter_IntersectCmd"
				Index = 2
			class Include3DGeometry:
				ID = "Include3DGeometry"
				Index = 3
				Include3DGeometry = AllControls.Include3DGeometry
			class SeparatorAfter_Include3DGeometry:
				ID = "SeparatorAfter_Include3DGeometry"
				Index = 4
			class ProjectToSurface:
				ID = "ProjectToSurface"
				Index = 5
				ProjectToSurface = AllControls.ProjectToSurface
			class IntersectionCurve:
				ID = "IntersectionCurve"
				Index = 6
				IntersectionCurve = AllControls.IntersectionCurve
		class SeparatorAfter_ProjectIncludeDropDown:
			ID = "SeparatorAfter_ProjectIncludeDropDown"
			Index = 20
		class SketchDimension:
			ID = "SketchDimension"
			Index = 21
			isPromoted = True
			isPromotedByDefault = True
			SketchDimension = AllControls.SketchDimension
		class SeparatorAfter_SketchDimension:
			ID = "SeparatorAfter_SketchDimension"
			Index = 22
	class PCB3DSketchCreatePanel:
		ID = "PCB3DSketchCreatePanel"
		class DrawPolyline:
			ID = "DrawPolyline"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			DrawPolyline = AllControls.DrawPolyline
		class RectangleDropDown:
			ID = "RectangleDropDown"
			Index = 1
			class ShapeRectangleTwoPoint:
				ID = "ShapeRectangleTwoPoint"
				Index = 0
				ShapeRectangleTwoPoint = AllControls.ShapeRectangleTwoPoint
			class ShapeRectangleThreePoint:
				ID = "ShapeRectangleThreePoint"
				Index = 1
				ShapeRectangleThreePoint = AllControls.ShapeRectangleThreePoint
			class ShapeRectangleCenter:
				ID = "ShapeRectangleCenter"
				Index = 2
				ShapeRectangleCenter = AllControls.ShapeRectangleCenter
		class CircleDropDown:
			ID = "CircleDropDown"
			Index = 2
			class CircleCenterRadius:
				ID = "CircleCenterRadius"
				Index = 0
				CircleCenterRadius = AllControls.CircleCenterRadius
			class CircleTwoPoint:
				ID = "CircleTwoPoint"
				Index = 1
				CircleTwoPoint = AllControls.CircleTwoPoint
			class CircleThreePoint:
				ID = "CircleThreePoint"
				Index = 2
				CircleThreePoint = AllControls.CircleThreePoint
			class CircleTanTanRadius:
				ID = "CircleTanTanRadius"
				Index = 3
				CircleTanTanRadius = AllControls.CircleTanTanRadius
			class CircleThreeTangent:
				ID = "CircleThreeTangent"
				Index = 4
				CircleThreeTangent = AllControls.CircleThreeTangent
		class ArcDropDown:
			ID = "ArcDropDown"
			Index = 3
			class ArcThreePoint:
				ID = "ArcThreePoint"
				Index = 0
				ArcThreePoint = AllControls.ArcThreePoint
			class ArcCenterTwoPoint:
				ID = "ArcCenterTwoPoint"
				Index = 1
				ArcCenterTwoPoint = AllControls.ArcCenterTwoPoint
			class ArcTangent:
				ID = "ArcTangent"
				Index = 2
				ArcTangent = AllControls.ArcTangent
		class PolygonDropDown:
			ID = "PolygonDropDown"
			Index = 4
			class ShapePolygonCircumscribed:
				ID = "ShapePolygonCircumscribed"
				Index = 0
				ShapePolygonCircumscribed = AllControls.ShapePolygonCircumscribed
			class ShapePolygonInscribed:
				ID = "ShapePolygonInscribed"
				Index = 1
				ShapePolygonInscribed = AllControls.ShapePolygonInscribed
			class ShapePolygonEdge:
				ID = "ShapePolygonEdge"
				Index = 2
				ShapePolygonEdge = AllControls.ShapePolygonEdge
		class SlotDropDown:
			ID = "SlotDropDown"
			Index = 5
			class ShapeSlotCenterToCenter:
				ID = "ShapeSlotCenterToCenter"
				Index = 0
				ShapeSlotCenterToCenter = AllControls.ShapeSlotCenterToCenter
			class ShapeSlotOverall:
				ID = "ShapeSlotOverall"
				Index = 1
				ShapeSlotOverall = AllControls.ShapeSlotOverall
			class ShapeSlotCenterPoint:
				ID = "ShapeSlotCenterPoint"
				Index = 2
				ShapeSlotCenterPoint = AllControls.ShapeSlotCenterPoint
			class ShapeArcSlotThreePoint:
				ID = "ShapeArcSlotThreePoint"
				Index = 3
				ShapeArcSlotThreePoint = AllControls.ShapeArcSlotThreePoint
			class ShapeArcSlotCenterTwoPoint:
				ID = "ShapeArcSlotCenterTwoPoint"
				Index = 4
				ShapeArcSlotCenterTwoPoint = AllControls.ShapeArcSlotCenterTwoPoint
		class SplineDropDown:
			ID = "SplineDropDown"
			Index = 6
			class DrawCVMSpline3D:
				ID = "DrawCVMSpline3D"
				Index = 0
				isPromoted = True
				isPromotedByDefault = True
				DrawCVMSpline3D = AllControls.DrawCVMSpline3D
		class ConicCurveCmd:
			ID = "ConicCurveCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			ConicCurveCmd = AllControls.ConicCurveCmd
		class DrawPoint:
			ID = "DrawPoint"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			DrawPoint = AllControls.DrawPoint
		class TextCmd:
			ID = "TextCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			TextCmd = AllControls.TextCmd
		class MTextCmd:
			ID = "MTextCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			MTextCmd = AllControls.MTextCmd
		class SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_MTextCmd"
			Index = 11
		class SeparatorAfter_SeparatorAfter_MTextCmd:
			ID = "SeparatorAfter_SeparatorAfter_MTextCmd"
			Index = 12
		class MirrorSketchCommand:
			ID = "MirrorSketchCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			MirrorSketchCommand = AllControls.MirrorSketchCommand
		class CircularSketchPatternCommand:
			ID = "CircularSketchPatternCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			CircularSketchPatternCommand = AllControls.CircularSketchPatternCommand
		class RectangularSketchPatternCommand:
			ID = "RectangularSketchPatternCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			RectangularSketchPatternCommand = AllControls.RectangularSketchPatternCommand
		class SeparatorAfter_RectangularSketchPatternCommand:
			ID = "SeparatorAfter_RectangularSketchPatternCommand"
			Index = 16
		class ProjectIncludeDropDown:
			ID = "ProjectIncludeDropDown"
			Index = 17
			class ProjectNewCmd:
				ID = "ProjectNewCmd"
				Index = 0
				ProjectNewCmd = AllControls.ProjectNewCmd
			class IntersectCmd:
				ID = "IntersectCmd"
				Index = 1
				IntersectCmd = AllControls.IntersectCmd
			class SeparatorAfter_IntersectCmd:
				ID = "SeparatorAfter_IntersectCmd"
				Index = 2
			class Include3DGeometry:
				ID = "Include3DGeometry"
				Index = 3
				Include3DGeometry = AllControls.Include3DGeometry
			class SeparatorAfter_Include3DGeometry:
				ID = "SeparatorAfter_Include3DGeometry"
				Index = 4
			class ProjectToSurface:
				ID = "ProjectToSurface"
				Index = 5
				ProjectToSurface = AllControls.ProjectToSurface
			class IntersectionCurve:
				ID = "IntersectionCurve"
				Index = 6
				IntersectionCurve = AllControls.IntersectionCurve
		class SeparatorAfter_ProjectIncludeDropDown:
			ID = "SeparatorAfter_ProjectIncludeDropDown"
			Index = 18
		class SketchDimension:
			ID = "SketchDimension"
			Index = 19
			isPromoted = True
			isPromotedByDefault = True
			SketchDimension = AllControls.SketchDimension
		class SeparatorAfter_SketchDimension:
			ID = "SeparatorAfter_SketchDimension"
			Index = 20
	class SketchModifyPanel:
		ID = "SketchModifyPanel"
		class FilletSketchCmd:
			ID = "FilletSketchCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FilletSketchCmd = AllControls.FilletSketchCmd
		class SketchChamferDropDown:
			ID = "SketchChamferDropDown"
			Index = 1
			class ChamferSketchEqualDistance:
				ID = "ChamferSketchEqualDistance"
				Index = 0
				ChamferSketchEqualDistance = AllControls.ChamferSketchEqualDistance
			class ChamferSketchDistanceAngle:
				ID = "ChamferSketchDistanceAngle"
				Index = 1
				ChamferSketchDistanceAngle = AllControls.ChamferSketchDistanceAngle
			class ChamferSketchDistanceDistance:
				ID = "ChamferSketchDistanceDistance"
				Index = 2
				ChamferSketchDistanceDistance = AllControls.ChamferSketchDistanceDistance
		class TrimSketchCmd:
			ID = "TrimSketchCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			TrimSketchCmd = AllControls.TrimSketchCmd
		class ExtendSketchCmd:
			ID = "ExtendSketchCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			ExtendSketchCmd = AllControls.ExtendSketchCmd
		class BreakSketchCmd:
			ID = "BreakSketchCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			BreakSketchCmd = AllControls.BreakSketchCmd
		class SketchScaleCmd:
			ID = "SketchScaleCmd"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			SketchScaleCmd = AllControls.SketchScaleCmd
		class Offset:
			ID = "Offset"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			Offset = AllControls.Offset
		class SeparatorAfter_Offset:
			ID = "SeparatorAfter_Offset"
			Index = 7
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
			FusionMoveCommand = AllControls.FusionMoveCommand
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
	class SketchConstraintsPanel:
		ID = "SketchConstraintsPanel"
		class ConstraintHorizontalVertical:
			ID = "ConstraintHorizontalVertical"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ConstraintHorizontalVertical = AllControls.ConstraintHorizontalVertical
		class ConstraintCoincident:
			ID = "ConstraintCoincident"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			ConstraintCoincident = AllControls.ConstraintCoincident
		class ConstraintTangent:
			ID = "ConstraintTangent"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			ConstraintTangent = AllControls.ConstraintTangent
		class ConstraintEqual:
			ID = "ConstraintEqual"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ConstraintEqual = AllControls.ConstraintEqual
		class ConstraintParallel:
			ID = "ConstraintParallel"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			ConstraintParallel = AllControls.ConstraintParallel
		class ConstraintPerpendicular:
			ID = "ConstraintPerpendicular"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			ConstraintPerpendicular = AllControls.ConstraintPerpendicular
		class ConstraintFix:
			ID = "ConstraintFix"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			ConstraintFix = AllControls.ConstraintFix
		class ConstraintMidPoint:
			ID = "ConstraintMidPoint"
			Index = 7
			isPromoted = True
			isPromotedByDefault = True
			ConstraintMidPoint = AllControls.ConstraintMidPoint
		class ConstraintConcentric:
			ID = "ConstraintConcentric"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			ConstraintConcentric = AllControls.ConstraintConcentric
		class ConstraintCollinear:
			ID = "ConstraintCollinear"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
			ConstraintCollinear = AllControls.ConstraintCollinear
		class ConstraintSymmetry:
			ID = "ConstraintSymmetry"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
			ConstraintSymmetry = AllControls.ConstraintSymmetry
		class ConstraintSmooth:
			ID = "ConstraintSmooth"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
			ConstraintSmooth = AllControls.ConstraintSmooth
	class SolidCreatePanel:
		ID = "SolidCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			SketchCreate = AllControls.SketchCreate
		class TSplineBaseFeatureCreationCommand:
			ID = "TSplineBaseFeatureCreationCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = True
			TSplineBaseFeatureCreationCommand = AllControls.TSplineBaseFeatureCreationCommand
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			PushDeriveCommand = AllControls.PushDeriveCommand
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 4
		class Extrude:
			ID = "Extrude"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			Extrude = AllControls.Extrude
		class Revolve:
			ID = "Revolve"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			Revolve = AllControls.Revolve
		class Sweep:
			ID = "Sweep"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			Sweep = AllControls.Sweep
		class SolidLoft:
			ID = "SolidLoft"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
			SolidLoft = AllControls.SolidLoft
		class FusionRibCommand:
			ID = "FusionRibCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionRibCommand = AllControls.FusionRibCommand
		class FusionWebCommand:
			ID = "FusionWebCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionWebCommand = AllControls.FusionWebCommand
		class EmbossCmd:
			ID = "EmbossCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			EmbossCmd = AllControls.EmbossCmd
		class SeparatorAfter_EmbossCmd:
			ID = "SeparatorAfter_EmbossCmd"
			Index = 12
		class FusionHoleCommand:
			ID = "FusionHoleCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			FusionHoleCommand = AllControls.FusionHoleCommand
		class FusionThreadCommand:
			ID = "FusionThreadCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionThreadCommand = AllControls.FusionThreadCommand
		class SeparatorAfter_FusionThreadCommand:
			ID = "SeparatorAfter_FusionThreadCommand"
			Index = 15
		class PrimitiveBox:
			ID = "PrimitiveBox"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			PrimitiveBox = AllControls.PrimitiveBox
		class PrimitiveCylinder:
			ID = "PrimitiveCylinder"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			PrimitiveCylinder = AllControls.PrimitiveCylinder
		class PrimitiveSphere:
			ID = "PrimitiveSphere"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			PrimitiveSphere = AllControls.PrimitiveSphere
		class PrimitiveTorus:
			ID = "PrimitiveTorus"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			PrimitiveTorus = AllControls.PrimitiveTorus
		class PrimitiveCoil:
			ID = "PrimitiveCoil"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			PrimitiveCoil = AllControls.PrimitiveCoil
		class PrimitivePipe:
			ID = "PrimitivePipe"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			PrimitivePipe = AllControls.PrimitivePipe
		class SeparatorAfter_PrimitivePipe:
			ID = "SeparatorAfter_PrimitivePipe"
			Index = 22
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 23
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
				PatternRectangular = AllControls.PatternRectangular
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
				PatternCircular = AllControls.PatternCircular
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
				PatternOnPath = AllControls.PatternOnPath
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 24
			isPromoted = True
			isPromotedByDefault = False
			MirrorCommand = AllControls.MirrorCommand
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 25
		class FusionSurfaceThickenCommand:
			ID = "FusionSurfaceThickenCommand"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceThickenCommand = AllControls.FusionSurfaceThickenCommand
		class SurfaceSculpt:
			ID = "SurfaceSculpt"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
			SurfaceSculpt = AllControls.SurfaceSculpt
		class SeparatorAfter_SurfaceSculpt:
			ID = "SeparatorAfter_SurfaceSculpt"
			Index = 28
		class FusionFindFeaturesCommand:
			ID = "FusionFindFeaturesCommand"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
			FusionFindFeaturesCommand = AllControls.FusionFindFeaturesCommand
		class EnclosureCommand:
			ID = "EnclosureCommand"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
			EnclosureCommand = AllControls.EnclosureCommand
		class SeparatorAfter_EnclosureCommand:
			ID = "SeparatorAfter_EnclosureCommand"
			Index = 31
		class MeshBaseFeatureCreationCommand:
			ID = "MeshBaseFeatureCreationCommand"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
			MeshBaseFeatureCreationCommand = AllControls.MeshBaseFeatureCreationCommand
		class MeshPlanarSectionCommand:
			ID = "MeshPlanarSectionCommand"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
			MeshPlanarSectionCommand = AllControls.MeshPlanarSectionCommand
		class SeparatorAfter_MeshPlanarSectionCommand:
			ID = "SeparatorAfter_MeshPlanarSectionCommand"
			Index = 34
		class BaseFeatureCreationCommand:
			ID = "BaseFeatureCreationCommand"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
			BaseFeatureCreationCommand = AllControls.BaseFeatureCreationCommand
		class PCBCreateCmd:
			ID = "PCBCreateCmd"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
			PCBCreateCmd = AllControls.PCBCreateCmd
		class PCBDeriveCmd:
			ID = "PCBDeriveCmd"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
			PCBDeriveCmd = AllControls.PCBDeriveCmd
	class GeneratePanel:
		ID = "GeneratePanel"
		class AutomatedModelingCommand:
			ID = "AutomatedModelingCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			AutomatedModelingCommand = AllControls.AutomatedModelingCommand
	class SolidModifyPanel:
		ID = "SolidModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionPressPullCommand = AllControls.FusionPressPullCommand
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			EditFaceCommand = AllControls.EditFaceCommand
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionFilletEdgesCommand = AllControls.FusionFilletEdgesCommand
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = False
			FusionChamferCommand = AllControls.FusionChamferCommand
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionShellBodyCommand:
			ID = "FusionShellBodyCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionShellBodyCommand = AllControls.FusionShellBodyCommand
		class FusionDraftCommand:
			ID = "FusionDraftCommand"
			Index = 7
			isPromoted = True
			isPromotedByDefault = False
			FusionDraftCommand = AllControls.FusionDraftCommand
		class ModifyScale:
			ID = "ModifyScale"
			Index = 8
			isPromoted = True
			isPromotedByDefault = False
			ModifyScale = AllControls.ModifyScale
		class FusionCombineCommand:
			ID = "FusionCombineCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
			FusionCombineCommand = AllControls.FusionCombineCommand
		class FusionOffsetFacesCommand:
			ID = "FusionOffsetFacesCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionOffsetFacesCommand = AllControls.FusionOffsetFacesCommand
		class FusionReplaceFaceCommand:
			ID = "FusionReplaceFaceCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionReplaceFaceCommand = AllControls.FusionReplaceFaceCommand
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionSplitFaceCommand = AllControls.FusionSplitFaceCommand
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			FusionSplitBodyCommand = AllControls.FusionSplitBodyCommand
		class FusionPartingLineSplitCmd:
			ID = "FusionPartingLineSplitCmd"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionPartingLineSplitCmd = AllControls.FusionPartingLineSplitCmd
		class SeparatorAfter_FusionPartingLineSplitCmd:
			ID = "SeparatorAfter_FusionPartingLineSplitCmd"
			Index = 15
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 19
		class ArrangeCommand:
			ID = "ArrangeCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			ArrangeCommand = AllControls.ArrangeCommand
		class SimplifyDropDown:
			ID = "SimplifyDropDown"
			Index = 21
			class FusionRemoveFeaturesCommand:
				ID = "FusionRemoveFeaturesCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				FusionRemoveFeaturesCommand = AllControls.FusionRemoveFeaturesCommand
			class FusionRemoveFacesCommand:
				ID = "FusionRemoveFacesCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				FusionRemoveFacesCommand = AllControls.FusionRemoveFacesCommand
			class ReplaceWithPrimitivesCommand:
				ID = "ReplaceWithPrimitivesCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				ReplaceWithPrimitivesCommand = AllControls.ReplaceWithPrimitivesCommand
		class SeparatorAfter_SimplifyDropDown:
			ID = "SeparatorAfter_SimplifyDropDown"
			Index = 22
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
			AppearanceCommand = AllControls.AppearanceCommand
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
			MaterialCommand = AllControls.MaterialCommand
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 26
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 27
			isPromoted = True
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 28
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 29
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
			TSpline2BRepCommand = AllControls.TSpline2BRepCommand
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 31
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				Mesh2BRepCommand = AllControls.Mesh2BRepCommand
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				BRep2MeshCommand = AllControls.BRep2MeshCommand
	class SheetMetalCreatePanel:
		ID = "SheetMetalCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			SketchCreate = AllControls.SketchCreate
		class FusionSheetMetalFlangeCommand:
			ID = "FusionSheetMetalFlangeCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionSheetMetalFlangeCommand = AllControls.FusionSheetMetalFlangeCommand
		class SheetMetalBendCmd:
			ID = "SheetMetalBendCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			SheetMetalBendCmd = AllControls.SheetMetalBendCmd
		class ConvertToSheetMetalCmd:
			ID = "ConvertToSheetMetalCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			ConvertToSheetMetalCmd = AllControls.ConvertToSheetMetalCmd
		class DMConvertToSheetMetalCmd:
			ID = "DMConvertToSheetMetalCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			DMConvertToSheetMetalCmd = AllControls.DMConvertToSheetMetalCmd
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			PushDeriveCommand = AllControls.PushDeriveCommand
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 7
		class Extrude:
			ID = "Extrude"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			Extrude = AllControls.Extrude
		class SeparatorAfter_Extrude:
			ID = "SeparatorAfter_Extrude"
			Index = 9
		class FusionHoleCommand:
			ID = "FusionHoleCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionHoleCommand = AllControls.FusionHoleCommand
		class FusionThreadCommand:
			ID = "FusionThreadCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionThreadCommand = AllControls.FusionThreadCommand
		class SeparatorAfter_FusionThreadCommand:
			ID = "SeparatorAfter_FusionThreadCommand"
			Index = 12
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 13
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
				PatternRectangular = AllControls.PatternRectangular
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
				PatternCircular = AllControls.PatternCircular
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
				PatternOnPath = AllControls.PatternOnPath
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			MirrorCommand = AllControls.MirrorCommand
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 15
		class FusionSheetMetalFlatPatternCmd:
			ID = "FusionSheetMetalFlatPatternCmd"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
			FusionSheetMetalFlatPatternCmd = AllControls.FusionSheetMetalFlatPatternCmd
	class SheetMetalModifyPanel:
		ID = "SheetMetalModifyPanel"
		class SeparatorAfter_:
			ID = "SeparatorAfter_"
			Index = 0
		class FusionSheetmetalUnfoldCommand:
			ID = "FusionSheetmetalUnfoldCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			FusionSheetmetalUnfoldCommand = AllControls.FusionSheetmetalUnfoldCommand
		class FusionSheetMetalRulesCommand:
			ID = "FusionSheetMetalRulesCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionSheetMetalRulesCommand = AllControls.FusionSheetMetalRulesCommand
		class SeparatorAfter_FusionSheetMetalRulesCommand:
			ID = "SeparatorAfter_FusionSheetMetalRulesCommand"
			Index = 3
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionFilletEdgesCommand = AllControls.FusionFilletEdgesCommand
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionChamferCommand = AllControls.FusionChamferCommand
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 6
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 10
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			AppearanceCommand = AllControls.AppearanceCommand
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			MaterialCommand = AllControls.MaterialCommand
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 14
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 17
	class AssemblePanel:
		ID = "AssemblePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class JointAssembleCmdNew:
			ID = "JointAssembleCmdNew"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			JointAssembleCmdNew = AllControls.JointAssembleCmdNew
		class JointAsBuiltCmd:
			ID = "JointAsBuiltCmd"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			JointAsBuiltCmd = AllControls.JointAsBuiltCmd
		class JointOrigin:
			ID = "JointOrigin"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			JointOrigin = AllControls.JointOrigin
		class RigidGroupCmd:
			ID = "RigidGroupCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			RigidGroupCmd = AllControls.RigidGroupCmd
		class SeparatorAfter_RigidGroupCmd:
			ID = "SeparatorAfter_RigidGroupCmd"
			Index = 5
		class FusionMoveJointsCommand:
			ID = "FusionMoveJointsCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionMoveJointsCommand = AllControls.FusionMoveJointsCommand
		class FusionMotionRelationshipCommand:
			ID = "FusionMotionRelationshipCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionMotionRelationshipCommand = AllControls.FusionMotionRelationshipCommand
		class SeparatorAfter_FusionMotionRelationshipCommand:
			ID = "SeparatorAfter_FusionMotionRelationshipCommand"
			Index = 8
		class EnableContactSetsCmd:
			ID = "EnableContactSetsCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			EnableContactSetsCmd = AllControls.EnableContactSetsCmd
		class EnableAllContactCmd:
			ID = "EnableAllContactCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			EnableAllContactCmd = AllControls.EnableAllContactCmd
		class DisableAllContactCmd:
			ID = "DisableAllContactCmd"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			DisableAllContactCmd = AllControls.DisableAllContactCmd
		class ContactSetCmd:
			ID = "ContactSetCmd"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			ContactSetCmd = AllControls.ContactSetCmd
		class SeparatorAfter_ContactSetCmd:
			ID = "SeparatorAfter_ContactSetCmd"
			Index = 13
		class FusionMotionStudyCommand:
			ID = "FusionMotionStudyCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionMotionStudyCommand = AllControls.FusionMotionStudyCommand
	class AssembleModifyPanel:
		ID = "AssembleModifyPanel"
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
	class AssembleUtilityPanel:
		ID = "AssembleUtilityPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			InterferenceCheckCommand = AllControls.InterferenceCheckCommand
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceValidateCommand = AllControls.FusionSurfaceValidateCommand
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 3
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureCombAnalysisCommand = AllControls.FusionCurvatureCombAnalysisCommand
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionZebraAnalysisCommand = AllControls.FusionZebraAnalysisCommand
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionDraftAnalysisCommand = AllControls.FusionDraftAnalysisCommand
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureMapAnalysisCommand = AllControls.FusionCurvatureMapAnalysisCommand
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			FusionAccessibilityAnalysisCommand = AllControls.FusionAccessibilityAnalysisCommand
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionMinimumRadiusAnalysisCommand = AllControls.FusionMinimumRadiusAnalysisCommand
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionHalfSectionViewCommand = AllControls.FusionHalfSectionViewCommand
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionCenterOfMassCommand = AllControls.FusionCenterOfMassCommand
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 12
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			FusionViewColorCyclingToggleCmd = AllControls.FusionViewColorCyclingToggleCmd
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
	class SurfaceCreatePanel:
		ID = "SurfaceCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			SketchCreate = AllControls.SketchCreate
		class PushDeriveCommand:
			ID = "PushDeriveCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			PushDeriveCommand = AllControls.PushDeriveCommand
		class SeparatorAfter_PushDeriveCommand:
			ID = "SeparatorAfter_PushDeriveCommand"
			Index = 3
		class SurfaceExtrude:
			ID = "SurfaceExtrude"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			SurfaceExtrude = AllControls.SurfaceExtrude
		class SurfaceRevolve:
			ID = "SurfaceRevolve"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			SurfaceRevolve = AllControls.SurfaceRevolve
		class SurfaceSweep:
			ID = "SurfaceSweep"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			SurfaceSweep = AllControls.SurfaceSweep
		class SurfaceLoft:
			ID = "SurfaceLoft"
			Index = 7
			isPromoted = True
			isPromotedByDefault = False
			SurfaceLoft = AllControls.SurfaceLoft
		class FusionSurfacePatchCommand:
			ID = "FusionSurfacePatchCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			FusionSurfacePatchCommand = AllControls.FusionSurfacePatchCommand
		class FusionSurfaceRuledCommand:
			ID = "FusionSurfaceRuledCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceRuledCommand = AllControls.FusionSurfaceRuledCommand
		class FusionSurfaceOffsetCommand:
			ID = "FusionSurfaceOffsetCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceOffsetCommand = AllControls.FusionSurfaceOffsetCommand
		class SeparatorAfter_FusionSurfaceOffsetCommand:
			ID = "SeparatorAfter_FusionSurfaceOffsetCommand"
			Index = 11
		class SurfPrimitiveBox:
			ID = "SurfPrimitiveBox"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitiveBox = AllControls.SurfPrimitiveBox
		class SurfPrimitiveCylinder:
			ID = "SurfPrimitiveCylinder"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitiveCylinder = AllControls.SurfPrimitiveCylinder
		class SurfPrimitiveSphere:
			ID = "SurfPrimitiveSphere"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitiveSphere = AllControls.SurfPrimitiveSphere
		class SurfPrimitiveTorus:
			ID = "SurfPrimitiveTorus"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitiveTorus = AllControls.SurfPrimitiveTorus
		class SurfPrimitiveCoil:
			ID = "SurfPrimitiveCoil"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitiveCoil = AllControls.SurfPrimitiveCoil
		class SurfPrimitivePipe:
			ID = "SurfPrimitivePipe"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			SurfPrimitivePipe = AllControls.SurfPrimitivePipe
		class SeparatorAfter_SurfPrimitivePipe:
			ID = "SeparatorAfter_SurfPrimitivePipe"
			Index = 18
		class PatternDropDown:
			ID = "PatternDropDown"
			Index = 19
			class PatternRectangular:
				ID = "PatternRectangular"
				Index = 0
				PatternRectangular = AllControls.PatternRectangular
			class PatternCircular:
				ID = "PatternCircular"
				Index = 1
				PatternCircular = AllControls.PatternCircular
			class PatternOnPath:
				ID = "PatternOnPath"
				Index = 2
				PatternOnPath = AllControls.PatternOnPath
		class MirrorCommand:
			ID = "MirrorCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			MirrorCommand = AllControls.MirrorCommand
		class SeparatorAfter_MirrorCommand:
			ID = "SeparatorAfter_MirrorCommand"
			Index = 21
		class FusionSurfaceThickenCommand:
			ID = "FusionSurfaceThickenCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceThickenCommand = AllControls.FusionSurfaceThickenCommand
		class SurfaceSculpt:
			ID = "SurfaceSculpt"
			Index = 23
			isPromoted = True
			isPromotedByDefault = False
			SurfaceSculpt = AllControls.SurfaceSculpt
	class SurfaceModifyPanel:
		ID = "SurfaceModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			FusionPressPullCommand = AllControls.FusionPressPullCommand
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			EditFaceCommand = AllControls.EditFaceCommand
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionFilletEdgesCommand = AllControls.FusionFilletEdgesCommand
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionChamferCommand = AllControls.FusionChamferCommand
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionSurfaceTrimCommand:
			ID = "FusionSurfaceTrimCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionSurfaceTrimCommand = AllControls.FusionSurfaceTrimCommand
		class FusionSurfaceUntrimCommand:
			ID = "FusionSurfaceUntrimCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceUntrimCommand = AllControls.FusionSurfaceUntrimCommand
		class FusionExtendCommand:
			ID = "FusionExtendCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			FusionExtendCommand = AllControls.FusionExtendCommand
		class FusionSurfaceStitchCommand:
			ID = "FusionSurfaceStitchCommand"
			Index = 9
			isPromoted = True
			isPromotedByDefault = True
			FusionSurfaceStitchCommand = AllControls.FusionSurfaceStitchCommand
		class FusionSurfaceUnStitchCommand:
			ID = "FusionSurfaceUnStitchCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
			FusionSurfaceUnStitchCommand = AllControls.FusionSurfaceUnStitchCommand
		class FusionSurfaceMergeCommand:
			ID = "FusionSurfaceMergeCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceMergeCommand = AllControls.FusionSurfaceMergeCommand
		class FusionSurfaceReverseNormalCommand:
			ID = "FusionSurfaceReverseNormalCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceReverseNormalCommand = AllControls.FusionSurfaceReverseNormalCommand
		class ModifyScale:
			ID = "ModifyScale"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			ModifyScale = AllControls.ModifyScale
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionSplitFaceCommand = AllControls.FusionSplitFaceCommand
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			FusionSplitBodyCommand = AllControls.FusionSplitBodyCommand
		class SeparatorAfter_FusionSplitBodyCommand:
			ID = "SeparatorAfter_FusionSplitBodyCommand"
			Index = 16
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 20
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			TSpline2BRepCommand = AllControls.TSpline2BRepCommand
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 22
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				Mesh2BRepCommand = AllControls.Mesh2BRepCommand
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				BRep2MeshCommand = AllControls.BRep2MeshCommand
		class SeparatorAfter_MeshDropDown:
			ID = "SeparatorAfter_MeshDropDown"
			Index = 23
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
			AppearanceCommand = AllControls.AppearanceCommand
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
			MaterialCommand = AllControls.MaterialCommand
		class SeparatorAfter_MaterialCommand:
			ID = "SeparatorAfter_MaterialCommand"
			Index = 27
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 28
			isPromoted = False
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
	class TSplinePrimitivePanel:
		ID = "TSplinePrimitivePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class SketchCreate:
			ID = "SketchCreate"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			SketchCreate = AllControls.SketchCreate
		class SeparatorAfter_SketchCreate:
			ID = "SeparatorAfter_SketchCreate"
			Index = 2
		class TSplinePrimitiveBoxCommand:
			ID = "TSplinePrimitiveBoxCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			TSplinePrimitiveBoxCommand = AllControls.TSplinePrimitiveBoxCommand
		class TSplinePrimitivePlaneCommand:
			ID = "TSplinePrimitivePlaneCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			TSplinePrimitivePlaneCommand = AllControls.TSplinePrimitivePlaneCommand
		class TSplinePrimitiveCylinderCommand:
			ID = "TSplinePrimitiveCylinderCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			TSplinePrimitiveCylinderCommand = AllControls.TSplinePrimitiveCylinderCommand
		class TSplinePrimitiveSphereCommand:
			ID = "TSplinePrimitiveSphereCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			TSplinePrimitiveSphereCommand = AllControls.TSplinePrimitiveSphereCommand
		class TSplinePrimitiveTorusCommand:
			ID = "TSplinePrimitiveTorusCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			TSplinePrimitiveTorusCommand = AllControls.TSplinePrimitiveTorusCommand
		class TSplinePrimitiveQuadBallCommand:
			ID = "TSplinePrimitiveQuadBallCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			TSplinePrimitiveQuadBallCommand = AllControls.TSplinePrimitiveQuadBallCommand
		class TSplinePrimitivePipe:
			ID = "TSplinePrimitivePipe"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			TSplinePrimitivePipe = AllControls.TSplinePrimitivePipe
		class SeparatorAfter_TSplinePrimitivePipe:
			ID = "SeparatorAfter_TSplinePrimitivePipe"
			Index = 10
		class TSplineAppendFaceCommand:
			ID = "TSplineAppendFaceCommand"
			Index = 11
			isPromoted = True
			isPromotedByDefault = True
			TSplineAppendFaceCommand = AllControls.TSplineAppendFaceCommand
		class SeparatorAfter_TSplineAppendFaceCommand:
			ID = "SeparatorAfter_TSplineAppendFaceCommand"
			Index = 12
		class TSplineExtrudeCommand:
			ID = "TSplineExtrudeCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			TSplineExtrudeCommand = AllControls.TSplineExtrudeCommand
		class TSplineRevolveCommand:
			ID = "TSplineRevolveCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			TSplineRevolveCommand = AllControls.TSplineRevolveCommand
		class TSplineSweepCommand:
			ID = "TSplineSweepCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			TSplineSweepCommand = AllControls.TSplineSweepCommand
		class TSplineLoft:
			ID = "TSplineLoft"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			TSplineLoft = AllControls.TSplineLoft
	class TSplineModifyPanel:
		ID = "TSplineModifyPanel"
		class TSplineEditCommand:
			ID = "TSplineEditCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			TSplineEditCommand = AllControls.TSplineEditCommand
		class TSplineEditByCurveCmd:
			ID = "TSplineEditByCurveCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			TSplineEditByCurveCmd = AllControls.TSplineEditByCurveCmd
		class SeparatorAfter_TSplineEditByCurveCmd:
			ID = "SeparatorAfter_TSplineEditByCurveCmd"
			Index = 2
		class TSplineInsertEdgeCommand:
			ID = "TSplineInsertEdgeCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			TSplineInsertEdgeCommand = AllControls.TSplineInsertEdgeCommand
		class TSplineSubsetCmd:
			ID = "TSplineSubsetCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			TSplineSubsetCmd = AllControls.TSplineSubsetCmd
		class TSplineInsertPointCommand:
			ID = "TSplineInsertPointCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			TSplineInsertPointCommand = AllControls.TSplineInsertPointCommand
		class SeparatorAfter_TSplineInsertPointCommand:
			ID = "SeparatorAfter_TSplineInsertPointCommand"
			Index = 6
		class TSplineMergeEdgeCmd:
			ID = "TSplineMergeEdgeCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			TSplineMergeEdgeCmd = AllControls.TSplineMergeEdgeCmd
		class TSplineBridgeSubDCmd:
			ID = "TSplineBridgeSubDCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			TSplineBridgeSubDCmd = AllControls.TSplineBridgeSubDCmd
		class TSplineFillHoleCmd:
			ID = "TSplineFillHoleCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			TSplineFillHoleCmd = AllControls.TSplineFillHoleCmd
		class TSplineEraseAndFillCmd:
			ID = "TSplineEraseAndFillCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			TSplineEraseAndFillCmd = AllControls.TSplineEraseAndFillCmd
		class TSplineWeldCommand:
			ID = "TSplineWeldCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			TSplineWeldCommand = AllControls.TSplineWeldCommand
		class TSplineUnWeldCommand:
			ID = "TSplineUnWeldCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			TSplineUnWeldCommand = AllControls.TSplineUnWeldCommand
		class SeparatorAfter_TSplineUnWeldCommand:
			ID = "SeparatorAfter_TSplineUnWeldCommand"
			Index = 13
		class TSplineCreasedEdgeCommand:
			ID = "TSplineCreasedEdgeCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			TSplineCreasedEdgeCommand = AllControls.TSplineCreasedEdgeCommand
		class TSplineUnCreaseEdgeCmd:
			ID = "TSplineUnCreaseEdgeCmd"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			TSplineUnCreaseEdgeCmd = AllControls.TSplineUnCreaseEdgeCmd
		class TSplineBevelEdgeCommand:
			ID = "TSplineBevelEdgeCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			TSplineBevelEdgeCommand = AllControls.TSplineBevelEdgeCommand
		class TSplineSlideEdgeCommand:
			ID = "TSplineSlideEdgeCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			TSplineSlideEdgeCommand = AllControls.TSplineSlideEdgeCommand
		class SeparatorAfter_TSplineSlideEdgeCommand:
			ID = "SeparatorAfter_TSplineSlideEdgeCommand"
			Index = 18
		class TSplineSmoothCmd:
			ID = "TSplineSmoothCmd"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			TSplineSmoothCmd = AllControls.TSplineSmoothCmd
		class TSplineCylindrifyCmd:
			ID = "TSplineCylindrifyCmd"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			TSplineCylindrifyCmd = AllControls.TSplineCylindrifyCmd
		class TSplinePullSubDCmd:
			ID = "TSplinePullSubDCmd"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			TSplinePullSubDCmd = AllControls.TSplinePullSubDCmd
		class TSplineFlattenSubDCmd:
			ID = "TSplineFlattenSubDCmd"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
			TSplineFlattenSubDCmd = AllControls.TSplineFlattenSubDCmd
		class TSplineStraightenCmd:
			ID = "TSplineStraightenCmd"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
			TSplineStraightenCmd = AllControls.TSplineStraightenCmd
		class TSplineMatchCmd:
			ID = "TSplineMatchCmd"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
			TSplineMatchCmd = AllControls.TSplineMatchCmd
		class TSplineInterpolateSubDCmd:
			ID = "TSplineInterpolateSubDCmd"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
			TSplineInterpolateSubDCmd = AllControls.TSplineInterpolateSubDCmd
		class SeparatorAfter_TSplineInterpolateSubDCmd:
			ID = "SeparatorAfter_TSplineInterpolateSubDCmd"
			Index = 26
		class TSplineThickenCommand:
			ID = "TSplineThickenCommand"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
			TSplineThickenCommand = AllControls.TSplineThickenCommand
		class SeparatorAfter_TSplineThickenCommand:
			ID = "SeparatorAfter_TSplineThickenCommand"
			Index = 28
		class FreezeDropDown:
			ID = "FreezeDropDown"
			Index = 29
			class TSplineFreezeCmd:
				ID = "TSplineFreezeCmd"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				TSplineFreezeCmd = AllControls.TSplineFreezeCmd
			class TSplineUnFreezeCmd:
				ID = "TSplineUnFreezeCmd"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				TSplineUnFreezeCmd = AllControls.TSplineUnFreezeCmd
		class SeparatorAfter_FreezeDropDown:
			ID = "SeparatorAfter_FreezeDropDown"
			Index = 30
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 31
			isPromoted = False
			isPromotedByDefault = False
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 34
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
			AppearanceCommand = AllControls.AppearanceCommand
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
			MaterialCommand = AllControls.MaterialCommand
	class TSplineSymmetryPanel:
		ID = "TSplineSymmetryPanel"
		class TSplineInternalMirrorSymmetryCmd:
			ID = "TSplineInternalMirrorSymmetryCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			TSplineInternalMirrorSymmetryCmd = AllControls.TSplineInternalMirrorSymmetryCmd
		class TSplineInternalCircularSymmetryCmd:
			ID = "TSplineInternalCircularSymmetryCmd"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			TSplineInternalCircularSymmetryCmd = AllControls.TSplineInternalCircularSymmetryCmd
		class SeparatorAfter_TSplineInternalCircularSymmetryCmd:
			ID = "SeparatorAfter_TSplineInternalCircularSymmetryCmd"
			Index = 2
		class TSplineReflectionMirrorSymmetryCmd:
			ID = "TSplineReflectionMirrorSymmetryCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			TSplineReflectionMirrorSymmetryCmd = AllControls.TSplineReflectionMirrorSymmetryCmd
		class TSplineReflectionCircularSymmetryCmd:
			ID = "TSplineReflectionCircularSymmetryCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			TSplineReflectionCircularSymmetryCmd = AllControls.TSplineReflectionCircularSymmetryCmd
		class SeparatorAfter_TSplineReflectionCircularSymmetryCmd:
			ID = "SeparatorAfter_TSplineReflectionCircularSymmetryCmd"
			Index = 5
		class TSplineClearSymmetryCommand:
			ID = "TSplineClearSymmetryCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			TSplineClearSymmetryCommand = AllControls.TSplineClearSymmetryCommand
		class TSplineIsolateSymmetryCmd:
			ID = "TSplineIsolateSymmetryCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			TSplineIsolateSymmetryCmd = AllControls.TSplineIsolateSymmetryCmd
	class TSplineUtilitiesPanel:
		ID = "TSplineUtilitiesPanel"
		class TSplineToggleTessModeCmd:
			ID = "TSplineToggleTessModeCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			TSplineToggleTessModeCmd = AllControls.TSplineToggleTessModeCmd
		class SeparatorAfter_TSplineToggleTessModeCmd:
			ID = "SeparatorAfter_TSplineToggleTessModeCmd"
			Index = 1
		class TSplineRepairBodyCmd:
			ID = "TSplineRepairBodyCmd"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			TSplineRepairBodyCmd = AllControls.TSplineRepairBodyCmd
		class TSplineMakeUniformCmd:
			ID = "TSplineMakeUniformCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			TSplineMakeUniformCmd = AllControls.TSplineMakeUniformCmd
		class SeparatorAfter_TSplineMakeUniformCmd:
			ID = "SeparatorAfter_TSplineMakeUniformCmd"
			Index = 4
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			TSpline2BRepCommand = AllControls.TSpline2BRepCommand
		class SeparatorAfter_TSpline2BRepCommand:
			ID = "SeparatorAfter_TSpline2BRepCommand"
			Index = 6
		class TSplineCapSettingCommand:
			ID = "TSplineCapSettingCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			TSplineCapSettingCommand = AllControls.TSplineCapSettingCommand
	class MeshPrimitivePanel:
		ID = "MeshPrimitivePanel"
		class InsertAlignMeshCommand:
			ID = "InsertAlignMeshCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			InsertAlignMeshCommand = AllControls.InsertAlignMeshCommand
		class BRep2MeshCommand:
			ID = "BRep2MeshCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			BRep2MeshCommand = AllControls.BRep2MeshCommand
	class MeshModifyPanel:
		ID = "MeshModifyPanel"
		class MeshRemeshCommand:
			ID = "MeshRemeshCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeshRemeshCommand = AllControls.MeshRemeshCommand
		class MeshReduceCommand:
			ID = "MeshReduceCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			MeshReduceCommand = AllControls.MeshReduceCommand
		class MeshMakeSolidCommand:
			ID = "MeshMakeSolidCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			MeshMakeSolidCommand = AllControls.MeshMakeSolidCommand
		class SeparatorAfter_MeshMakeSolidCommand:
			ID = "SeparatorAfter_MeshMakeSolidCommand"
			Index = 3
		class MeshReplaceCommand:
			ID = "MeshReplaceCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			MeshReplaceCommand = AllControls.MeshReplaceCommand
		class MeshSmoothCommand:
			ID = "MeshSmoothCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			MeshSmoothCommand = AllControls.MeshSmoothCommand
		class MeshPlaneCutCommand:
			ID = "MeshPlaneCutCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			MeshPlaneCutCommand = AllControls.MeshPlaneCutCommand
		class MeshReverseNormalsCommand:
			ID = "MeshReverseNormalsCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			MeshReverseNormalsCommand = AllControls.MeshReverseNormalsCommand
		class MeshDeleteTrianglesCommand:
			ID = "MeshDeleteTrianglesCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			MeshDeleteTrianglesCommand = AllControls.MeshDeleteTrianglesCommand
		class SeparatorAfter_MeshDeleteTrianglesCommand:
			ID = "SeparatorAfter_MeshDeleteTrianglesCommand"
			Index = 9
		class MeshSubsetCommand:
			ID = "MeshSubsetCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			MeshSubsetCommand = AllControls.MeshSubsetCommand
		class MeshCombineCommand:
			ID = "MeshCombineCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			MeshCombineCommand = AllControls.MeshCombineCommand
		class SeparatorAfter_MeshCombineCommand:
			ID = "SeparatorAfter_MeshCombineCommand"
			Index = 12
		class FaceGroupsDropDown:
			ID = "FaceGroupsDropDown"
			Index = 13
			class MeshGenerateFGCommand:
				ID = "MeshGenerateFGCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				MeshGenerateFGCommand = AllControls.MeshGenerateFGCommand
			class MeshCreateFGCommand:
				ID = "MeshCreateFGCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				MeshCreateFGCommand = AllControls.MeshCreateFGCommand
			class MeshClearFGCommand:
				ID = "MeshClearFGCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				MeshClearFGCommand = AllControls.MeshClearFGCommand
		class SeparatorAfter_FaceGroupsDropDown:
			ID = "SeparatorAfter_FaceGroupsDropDown"
			Index = 14
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class ModifyScale:
			ID = "ModifyScale"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			ModifyScale = AllControls.ModifyScale
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
	class PCBCreatePanel:
		ID = "PCBCreatePanel"
		class FusionCreateNewComponentCommand:
			ID = "FusionCreateNewComponentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionCreateNewComponentCommand = AllControls.FusionCreateNewComponentCommand
		class SeparatorAfter_FusionCreateNewComponentCommand:
			ID = "SeparatorAfter_FusionCreateNewComponentCommand"
			Index = 1
		class PCBCreateCmd:
			ID = "PCBCreateCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PCBCreateCmd = AllControls.PCBCreateCmd
		class PCBDefineBoardCmd:
			ID = "PCBDefineBoardCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			PCBDefineBoardCmd = AllControls.PCBDefineBoardCmd
	class PCBModifyPanel:
		ID = "PCBModifyPanel"
		class PCBImprintCmd:
			ID = "PCBImprintCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PCBImprintCmd = AllControls.PCBImprintCmd
		class PCBBoardSketchEditCmd:
			ID = "PCBBoardSketchEditCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PCBBoardSketchEditCmd = AllControls.PCBBoardSketchEditCmd
		class PCBMoveComponentsCmd:
			ID = "PCBMoveComponentsCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PCBMoveComponentsCmd = AllControls.PCBMoveComponentsCmd
		class PCBFlipComponentCmd:
			ID = "PCBFlipComponentCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			PCBFlipComponentCmd = AllControls.PCBFlipComponentCmd
		class PCBStatusCmd:
			ID = "PCBStatusCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			PCBStatusCmd = AllControls.PCBStatusCmd
	class PCB3DPanel:
		ID = "PCB3DPanel"
		class PCB3DFlipComponentCmd:
			ID = "PCB3DFlipComponentCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PCB3DFlipComponentCmd = AllControls.PCB3DFlipComponentCmd
		class PCB3DMoveComponentsCmd:
			ID = "PCB3DMoveComponentsCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PCB3DMoveComponentsCmd = AllControls.PCB3DMoveComponentsCmd
		class PCBExportBrdCmd:
			ID = "PCBExportBrdCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PCBExportBrdCmd = AllControls.PCBExportBrdCmd
		class PCBLinkToBrdCmd:
			ID = "PCBLinkToBrdCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			PCBLinkToBrdCmd = AllControls.PCBLinkToBrdCmd
		class PCBHoleCmd:
			ID = "PCBHoleCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			PCBHoleCmd = AllControls.PCBHoleCmd
	class ConstructionPanel:
		ID = "ConstructionPanel"
		class WorkPlaneOffsetFromPlaneCommand:
			ID = "WorkPlaneOffsetFromPlaneCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			WorkPlaneOffsetFromPlaneCommand = AllControls.WorkPlaneOffsetFromPlaneCommand
		class WorkPlaneFromLineAndAngleCommand:
			ID = "WorkPlaneFromLineAndAngleCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
			WorkPlaneFromLineAndAngleCommand = AllControls.WorkPlaneFromLineAndAngleCommand
		class WorkPlaneTangentToCylinderCommand:
			ID = "WorkPlaneTangentToCylinderCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneTangentToCylinderCommand = AllControls.WorkPlaneTangentToCylinderCommand
		class WorkPlaneFromTwoPlanesCommand:
			ID = "WorkPlaneFromTwoPlanesCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = False
			WorkPlaneFromTwoPlanesCommand = AllControls.WorkPlaneFromTwoPlanesCommand
		class WorkPlaneFromTwoLinesCommand:
			ID = "WorkPlaneFromTwoLinesCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneFromTwoLinesCommand = AllControls.WorkPlaneFromTwoLinesCommand
		class WorkPlaneFromThreePointsCommand:
			ID = "WorkPlaneFromThreePointsCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneFromThreePointsCommand = AllControls.WorkPlaneFromThreePointsCommand
		class WorkPlaneFromPointAndFaceCommand:
			ID = "WorkPlaneFromPointAndFaceCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneFromPointAndFaceCommand = AllControls.WorkPlaneFromPointAndFaceCommand
		class WorkPlaneAlongPathCommand:
			ID = "WorkPlaneAlongPathCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneAlongPathCommand = AllControls.WorkPlaneAlongPathCommand
		class WorkPlaneFromPointAndNormalCommand:
			ID = "WorkPlaneFromPointAndNormalCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			WorkPlaneFromPointAndNormalCommand = AllControls.WorkPlaneFromPointAndNormalCommand
		class SeparatorAfter_WorkPlaneFromPointAndNormalCommand:
			ID = "SeparatorAfter_WorkPlaneFromPointAndNormalCommand"
			Index = 9
		class WorkAxisThroughCylinderCommand:
			ID = "WorkAxisThroughCylinderCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisThroughCylinderCommand = AllControls.WorkAxisThroughCylinderCommand
		class WorkAxisNormalToFaceCommand:
			ID = "WorkAxisNormalToFaceCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisNormalToFaceCommand = AllControls.WorkAxisNormalToFaceCommand
		class WorkAxisFromTwoPlanesCommand:
			ID = "WorkAxisFromTwoPlanesCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisFromTwoPlanesCommand = AllControls.WorkAxisFromTwoPlanesCommand
		class WorkAxisFromTwoPointsCommand:
			ID = "WorkAxisFromTwoPointsCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisFromTwoPointsCommand = AllControls.WorkAxisFromTwoPointsCommand
		class WorkAxisFromLineCommand:
			ID = "WorkAxisFromLineCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisFromLineCommand = AllControls.WorkAxisFromLineCommand
		class WorkAxisFromPointAndFaceCommand:
			ID = "WorkAxisFromPointAndFaceCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			WorkAxisFromPointAndFaceCommand = AllControls.WorkAxisFromPointAndFaceCommand
		class SeparatorAfter_WorkAxisFromPointAndFaceCommand:
			ID = "SeparatorAfter_WorkAxisFromPointAndFaceCommand"
			Index = 16
		class WorkPointFromPointCommand:
			ID = "WorkPointFromPointCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromPointCommand = AllControls.WorkPointFromPointCommand
		class WorkPointFromTwoLinesCommand:
			ID = "WorkPointFromTwoLinesCommand"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromTwoLinesCommand = AllControls.WorkPointFromTwoLinesCommand
		class WorkPointFromThreePlanesCommand:
			ID = "WorkPointFromThreePlanesCommand"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromThreePlanesCommand = AllControls.WorkPointFromThreePlanesCommand
		class WorkPointFromCircleOrSphereCommand:
			ID = "WorkPointFromCircleOrSphereCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromCircleOrSphereCommand = AllControls.WorkPointFromCircleOrSphereCommand
		class WorkPointFromLineAndPlaneCommand:
			ID = "WorkPointFromLineAndPlaneCommand"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromLineAndPlaneCommand = AllControls.WorkPointFromLineAndPlaneCommand
		class WorkPointAlongPathCommand:
			ID = "WorkPointAlongPathCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
			WorkPointAlongPathCommand = AllControls.WorkPointAlongPathCommand
		class WorkPointFromCoordsCommand:
			ID = "WorkPointFromCoordsCommand"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
			WorkPointFromCoordsCommand = AllControls.WorkPointFromCoordsCommand
	class InspectPanel:
		ID = "InspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class InterferenceCheckCommand:
			ID = "InterferenceCheckCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			InterferenceCheckCommand = AllControls.InterferenceCheckCommand
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceValidateCommand = AllControls.FusionSurfaceValidateCommand
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 3
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureCombAnalysisCommand = AllControls.FusionCurvatureCombAnalysisCommand
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionZebraAnalysisCommand = AllControls.FusionZebraAnalysisCommand
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionDraftAnalysisCommand = AllControls.FusionDraftAnalysisCommand
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureMapAnalysisCommand = AllControls.FusionCurvatureMapAnalysisCommand
		class FusionIsoCurveAnalysisCommand:
			ID = "FusionIsoCurveAnalysisCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			FusionIsoCurveAnalysisCommand = AllControls.FusionIsoCurveAnalysisCommand
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionAccessibilityAnalysisCommand = AllControls.FusionAccessibilityAnalysisCommand
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionMinimumRadiusAnalysisCommand = AllControls.FusionMinimumRadiusAnalysisCommand
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionHalfSectionViewCommand = AllControls.FusionHalfSectionViewCommand
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionCenterOfMassCommand = AllControls.FusionCenterOfMassCommand
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 13
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionViewColorCyclingToggleCmd = AllControls.FusionViewColorCyclingToggleCmd
	class InspectMeshPanel:
		ID = "InspectMeshPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class SeparatorAfter_MeasureCommand:
			ID = "SeparatorAfter_MeasureCommand"
			Index = 1
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionHalfSectionViewCommand = AllControls.FusionHalfSectionViewCommand
	class ToolsInspectPanel:
		ID = "ToolsInspectPanel"
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class FusionSurfaceValidateCommand:
			ID = "FusionSurfaceValidateCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			FusionSurfaceValidateCommand = AllControls.FusionSurfaceValidateCommand
		class SeparatorAfter_FusionSurfaceValidateCommand:
			ID = "SeparatorAfter_FusionSurfaceValidateCommand"
			Index = 2
		class FusionCurvatureCombAnalysisCommand:
			ID = "FusionCurvatureCombAnalysisCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureCombAnalysisCommand = AllControls.FusionCurvatureCombAnalysisCommand
		class FusionZebraAnalysisCommand:
			ID = "FusionZebraAnalysisCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionZebraAnalysisCommand = AllControls.FusionZebraAnalysisCommand
		class FusionDraftAnalysisCommand:
			ID = "FusionDraftAnalysisCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			FusionDraftAnalysisCommand = AllControls.FusionDraftAnalysisCommand
		class FusionCurvatureMapAnalysisCommand:
			ID = "FusionCurvatureMapAnalysisCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionCurvatureMapAnalysisCommand = AllControls.FusionCurvatureMapAnalysisCommand
		class FusionIsoCurveAnalysisCommand:
			ID = "FusionIsoCurveAnalysisCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionIsoCurveAnalysisCommand = AllControls.FusionIsoCurveAnalysisCommand
		class FusionAccessibilityAnalysisCommand:
			ID = "FusionAccessibilityAnalysisCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			FusionAccessibilityAnalysisCommand = AllControls.FusionAccessibilityAnalysisCommand
		class FusionMinimumRadiusAnalysisCommand:
			ID = "FusionMinimumRadiusAnalysisCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionMinimumRadiusAnalysisCommand = AllControls.FusionMinimumRadiusAnalysisCommand
		class FusionHalfSectionViewCommand:
			ID = "FusionHalfSectionViewCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
			FusionHalfSectionViewCommand = AllControls.FusionHalfSectionViewCommand
		class FusionCenterOfMassCommand:
			ID = "FusionCenterOfMassCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionCenterOfMassCommand = AllControls.FusionCenterOfMassCommand
		class SeparatorAfter_FusionCenterOfMassCommand:
			ID = "SeparatorAfter_FusionCenterOfMassCommand"
			Index = 12
		class FusionViewColorCyclingToggleCmd:
			ID = "FusionViewColorCyclingToggleCmd"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			FusionViewColorCyclingToggleCmd = AllControls.FusionViewColorCyclingToggleCmd
	class InsertPanel:
		ID = "InsertPanel"
		class InsertDialogCommand:
			ID = "InsertDialogCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			InsertDialogCommand = AllControls.InsertDialogCommand
		class PullDeriveCommand:
			ID = "PullDeriveCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = False
			PullDeriveCommand = AllControls.PullDeriveCommand
		class FusionAddEditDecalCommand:
			ID = "FusionAddEditDecalCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionAddEditDecalCommand = AllControls.FusionAddEditDecalCommand
		class FusionAddCanvasCommand:
			ID = "FusionAddCanvasCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionAddCanvasCommand = AllControls.FusionAddCanvasCommand
		class FusionAddBackgroundCanvasCommand:
			ID = "FusionAddBackgroundCanvasCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionAddBackgroundCanvasCommand = AllControls.FusionAddBackgroundCanvasCommand
		class SeparatorAfter_FusionAddBackgroundCanvasCommand:
			ID = "SeparatorAfter_FusionAddBackgroundCanvasCommand"
			Index = 5
		class TSplineImportCommand:
			ID = "TSplineImportCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			TSplineImportCommand = AllControls.TSplineImportCommand
		class SketchImportSVG:
			ID = "SketchImportSVG"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			SketchImportSVG = AllControls.SketchImportSVG
		class ImportDxfFileCommand:
			ID = "ImportDxfFileCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			ImportDxfFileCommand = AllControls.ImportDxfFileCommand
		class InsertMcMasterCarrComponentCommand:
			ID = "InsertMcMasterCarrComponentCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			InsertMcMasterCarrComponentCommand = AllControls.InsertMcMasterCarrComponentCommand
		class ParaMeshInsertAlignCommand:
			ID = "ParaMeshInsertAlignCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = False
			ParaMeshInsertAlignCommand = AllControls.ParaMeshInsertAlignCommand
		class cadenasparts4cad:
			ID = "cadenasparts4cad"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			cadenasparts4cad = AllControls.cadenasparts4cad
		class traceparts_insert:
			ID = "traceparts_insert"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			traceparts_insert = AllControls.traceparts_insert
	class StopPackagePanel:
		ID = "StopPackagePanel"
		class Package3DStop:
			ID = "Package3DStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			Package3DStop = AllControls.Package3DStop
	class ReturnLibraryPanel:
		ID = "ReturnLibraryPanel"
		class ReturnLibrary:
			ID = "ReturnLibrary"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
	class PackagePanel:
		ID = "PackagePanel"
		class PackageInsertCommand:
			ID = "PackageInsertCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
		class PackageFlipCommand:
			ID = "PackageFlipCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
		class PackageMoveCommand:
			ID = "PackageMoveCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
	class Package3DPanel:
		ID = "Package3DPanel"
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class MeasureCommand:
			ID = "MeasureCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			MeasureCommand = AllControls.MeasureCommand
		class PackageGenerator:
			ID = "PackageGenerator"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			PackageGenerator = AllControls.PackageGenerator
		class cmd_id_Axial:
			ID = "cmd_id_Axial"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Axial = AllControls.cmd_id_Axial
		class cmd_id_BGA:
			ID = "cmd_id_BGA"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_BGA = AllControls.cmd_id_BGA
		class cmd_id_Chip:
			ID = "cmd_id_Chip"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Chip = AllControls.cmd_id_Chip
		class cmd_id_Soic:
			ID = "cmd_id_Soic"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Soic = AllControls.cmd_id_Soic
		class cmd_id_DFN2:
			ID = "cmd_id_DFN2"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_DFN2 = AllControls.cmd_id_DFN2
		class cmd_id_DFN3:
			ID = "cmd_id_DFN3"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_DFN3 = AllControls.cmd_id_DFN3
		class cmd_id_DFN4:
			ID = "cmd_id_DFN4"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_DFN4 = AllControls.cmd_id_DFN4
		class cmd_id_header_right_angle:
			ID = "cmd_id_header_right_angle"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_header_right_angle = AllControls.cmd_id_header_right_angle
		class cmd_id_header_right_angle_socket:
			ID = "cmd_id_header_right_angle_socket"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_header_right_angle_socket = AllControls.cmd_id_header_right_angle_socket
		class cmd_id_header_straight:
			ID = "cmd_id_header_straight"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_header_straight = AllControls.cmd_id_header_straight
		class cmd_id_header_straight_socket:
			ID = "cmd_id_header_straight_socket"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_header_straight_socket = AllControls.cmd_id_header_straight_socket
		class cmd_id_Son:
			ID = "cmd_id_Son"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Son = AllControls.cmd_id_Son
		class cmd_id_Chip_led:
			ID = "cmd_id_Chip_led"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Chip_led = AllControls.cmd_id_Chip_led
		class cmd_id_Qfp:
			ID = "cmd_id_Qfp"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Qfp = AllControls.cmd_id_Qfp
		class cmd_id_Qfn:
			ID = "cmd_id_Qfn"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Qfn = AllControls.cmd_id_Qfn
		class cmd_id_chiparray_2side_convex:
			ID = "cmd_id_chiparray_2side_convex"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_chiparray_2side_convex = AllControls.cmd_id_chiparray_2side_convex
		class cmd_id_chiparray_2side_flat_concave:
			ID = "cmd_id_chiparray_2side_flat_concave"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_chiparray_2side_flat_concave = AllControls.cmd_id_chiparray_2side_flat_concave
		class cmd_id_chiparray_4side_flat:
			ID = "cmd_id_chiparray_4side_flat"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_chiparray_4side_flat = AllControls.cmd_id_chiparray_4side_flat
		class cmd_id_sot143:
			ID = "cmd_id_sot143"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_sot143 = AllControls.cmd_id_sot143
		class cmd_id_sot223:
			ID = "cmd_id_sot223"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_sot223 = AllControls.cmd_id_sot223
		class cmd_id_sot23:
			ID = "cmd_id_sot23"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_sot23 = AllControls.cmd_id_sot23
		class cmd_id_sotfl:
			ID = "cmd_id_sotfl"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_sotfl = AllControls.cmd_id_sotfl
		class cmd_id_Plcc:
			ID = "cmd_id_Plcc"
			Index = 25
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Plcc = AllControls.cmd_id_Plcc
		class cmd_id_Oscillator_j:
			ID = "cmd_id_Oscillator_j"
			Index = 26
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Oscillator_j = AllControls.cmd_id_Oscillator_j
		class cmd_id_Oscillator_l:
			ID = "cmd_id_Oscillator_l"
			Index = 27
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Oscillator_l = AllControls.cmd_id_Oscillator_l
		class cmd_id_Soj:
			ID = "cmd_id_Soj"
			Index = 28
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Soj = AllControls.cmd_id_Soj
		class cmd_id_crystal:
			ID = "cmd_id_crystal"
			Index = 29
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_crystal = AllControls.cmd_id_crystal
		class cmd_id_crystal_hc49:
			ID = "cmd_id_crystal_hc49"
			Index = 30
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_crystal_hc49 = AllControls.cmd_id_crystal_hc49
		class cmd_id_dip:
			ID = "cmd_id_dip"
			Index = 31
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_dip = AllControls.cmd_id_dip
		class cmd_id_ecap:
			ID = "cmd_id_ecap"
			Index = 32
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_ecap = AllControls.cmd_id_ecap
		class cmd_id_Melf:
			ID = "cmd_id_Melf"
			Index = 33
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Melf = AllControls.cmd_id_Melf
		class cmd_id_Molded:
			ID = "cmd_id_Molded"
			Index = 34
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Molded = AllControls.cmd_id_Molded
		class cmd_id_female_standoff:
			ID = "cmd_id_female_standoff"
			Index = 35
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_female_standoff = AllControls.cmd_id_female_standoff
		class cmd_id_male_female_standoff:
			ID = "cmd_id_male_female_standoff"
			Index = 36
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_male_female_standoff = AllControls.cmd_id_male_female_standoff
		class cmd_id_Sod:
			ID = "cmd_id_Sod"
			Index = 37
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Sod = AllControls.cmd_id_Sod
		class cmd_id_Snaplock:
			ID = "cmd_id_Snaplock"
			Index = 38
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Snaplock = AllControls.cmd_id_Snaplock
		class cmd_id_Radial:
			ID = "cmd_id_Radial"
			Index = 39
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Radial = AllControls.cmd_id_Radial
		class cmd_id_Radial_Round_Led:
			ID = "cmd_id_Radial_Round_Led"
			Index = 40
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Radial_Round_Led = AllControls.cmd_id_Radial_Round_Led
		class cmd_id_Cornerconcave:
			ID = "cmd_id_Cornerconcave"
			Index = 41
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Cornerconcave = AllControls.cmd_id_Cornerconcave
		class cmd_id_Sodfl:
			ID = "cmd_id_Sodfl"
			Index = 42
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_Sodfl = AllControls.cmd_id_Sodfl
		class cmd_id_TODPAK:
			ID = "cmd_id_TODPAK"
			Index = 43
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_TODPAK = AllControls.cmd_id_TODPAK
		class cmd_id_surafce_mount_header_female:
			ID = "cmd_id_surafce_mount_header_female"
			Index = 44
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_surafce_mount_header_female = AllControls.cmd_id_surafce_mount_header_female
		class cmd_id_surface_mount_pin_header_male:
			ID = "cmd_id_surface_mount_pin_header_male"
			Index = 45
			isPromoted = False
			isPromotedByDefault = False
			cmd_id_surface_mount_pin_header_male = AllControls.cmd_id_surface_mount_pin_header_male
	class MakePanel:
		ID = "MakePanel"
		class ThreeDprintCmdDef:
			ID = "ThreeDprintCmdDef"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ThreeDprintCmdDef = AllControls.ThreeDprintCmdDef
	class SolidScriptsAddinsPanel:
		ID = "SolidScriptsAddinsPanel"
		class ScriptsManagerCommand:
			ID = "ScriptsManagerCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ScriptsManagerCommand = AllControls.ScriptsManagerCommand
		class ExchangeAppStoreCommand:
			ID = "ExchangeAppStoreCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			ExchangeAppStoreCommand = AllControls.ExchangeAppStoreCommand
		class ExportToUnity_hellion:
			ID = "ExportToUnity_hellion"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			ExportToUnity_hellion = AllControls.ExportToUnity_hellion
		class cmdID_demo_1:
			ID = "cmdID_demo_1"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			cmdID_demo_1 = AllControls.cmdID_demo_1
		class OpenFoldersseparatorTop:
			ID = "OpenFoldersseparatorTop"
			Index = 4
		class OpenFoldersrootDropdown:
			ID = "OpenFoldersrootDropdown"
			Index = 5
			class OpenFoldersFusionInstall:
				ID = "OpenFoldersFusionInstall"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersFusionInstall = AllControls.OpenFoldersFusionInstall
			class OpenFoldersFusionApi:
				ID = "OpenFoldersFusionApi"
				Index = 1
				class OpenFoldersFusionApiCpp:
					ID = "OpenFoldersFusionApiCpp"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersFusionApiCpp = AllControls.OpenFoldersFusionApiCpp
				class OpenFoldersFusionApiPython:
					ID = "OpenFoldersFusionApiPython"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersFusionApiPython = AllControls.OpenFoldersFusionApiPython
			class OpenFoldersFusionPython:
				ID = "OpenFoldersFusionPython"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersFusionPython = AllControls.OpenFoldersFusionPython
			class OpenFoldersFusionPythonseparator:
				ID = "OpenFoldersFusionPythonseparator"
				Index = 3
			class OpenFoldersAutodesk:
				ID = "OpenFoldersAutodesk"
				Index = 4
				class OpenFoldersAutodeskLocal:
					ID = "OpenFoldersAutodeskLocal"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersAutodeskLocal = AllControls.OpenFoldersAutodeskLocal
				class OpenFoldersAutodeskRoaming:
					ID = "OpenFoldersAutodeskRoaming"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersAutodeskRoaming = AllControls.OpenFoldersAutodeskRoaming
			class OpenFoldersAutodeskseparator:
				ID = "OpenFoldersAutodeskseparator"
				Index = 5
			class OpenFoldersDesktop:
				ID = "OpenFoldersDesktop"
				Index = 6
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersDesktop = AllControls.OpenFoldersDesktop
			class OpenFoldersTempFiles:
				ID = "OpenFoldersTempFiles"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersTempFiles = AllControls.OpenFoldersTempFiles
			class OpenFoldersAppdata:
				ID = "OpenFoldersAppdata"
				Index = 8
				class OpenFoldersAppdataLocal:
					ID = "OpenFoldersAppdataLocal"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersAppdataLocal = AllControls.OpenFoldersAppdataLocal
				class OpenFoldersAppdataRoaming:
					ID = "OpenFoldersAppdataRoaming"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
					OpenFoldersAppdataRoaming = AllControls.OpenFoldersAppdataRoaming
			class OpenFoldersAppdataseparator:
				ID = "OpenFoldersAppdataseparator"
				Index = 9
			class OpenFoldersSettings:
				ID = "OpenFoldersSettings"
				Index = 10
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersSettings = AllControls.OpenFoldersSettings
			class OpenFoldersSettingsseparator:
				ID = "OpenFoldersSettingsseparator"
				Index = 11
		class OpenFoldersrootDropdownUndoc:
			ID = "OpenFoldersrootDropdownUndoc"
			Index = 6
			class OpenFoldersRootDirectory:
				ID = "OpenFoldersRootDirectory"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersRootDirectory = AllControls.OpenFoldersRootDirectory
			class OpenFoldersExecutableDirectory:
				ID = "OpenFoldersExecutableDirectory"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersExecutableDirectory = AllControls.OpenFoldersExecutableDirectory
			class OpenFoldersLocalizationDirectory:
				ID = "OpenFoldersLocalizationDirectory"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersLocalizationDirectory = AllControls.OpenFoldersLocalizationDirectory
			class OpenFoldersCoreAddInDirectory:
				ID = "OpenFoldersCoreAddInDirectory"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersCoreAddInDirectory = AllControls.OpenFoldersCoreAddInDirectory
			class OpenFoldersStringTableDirectory:
				ID = "OpenFoldersStringTableDirectory"
				Index = 4
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersStringTableDirectory = AllControls.OpenFoldersStringTableDirectory
			class OpenFoldersAppDirectory:
				ID = "OpenFoldersAppDirectory"
				Index = 5
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAppDirectory = AllControls.OpenFoldersAppDirectory
			class OpenFoldersSharedExtensionDirectory:
				ID = "OpenFoldersSharedExtensionDirectory"
				Index = 6
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersSharedExtensionDirectory = AllControls.OpenFoldersSharedExtensionDirectory
			class OpenFoldersTemporaryDirectory:
				ID = "OpenFoldersTemporaryDirectory"
				Index = 7
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersTemporaryDirectory = AllControls.OpenFoldersTemporaryDirectory
			class OpenFoldersUnbrandedUserDataDirectory:
				ID = "OpenFoldersUnbrandedUserDataDirectory"
				Index = 8
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersUnbrandedUserDataDirectory = AllControls.OpenFoldersUnbrandedUserDataDirectory
			class OpenFoldersUserDataDirectory:
				ID = "OpenFoldersUserDataDirectory"
				Index = 9
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersUserDataDirectory = AllControls.OpenFoldersUserDataDirectory
			class OpenFoldersAllUsersDataDirectory:
				ID = "OpenFoldersAllUsersDataDirectory"
				Index = 10
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAllUsersDataDirectory = AllControls.OpenFoldersAllUsersDataDirectory
			class OpenFoldersUnbrandedUserAppPluginsDirectory:
				ID = "OpenFoldersUnbrandedUserAppPluginsDirectory"
				Index = 11
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersUnbrandedUserAppPluginsDirectory = AllControls.OpenFoldersUnbrandedUserAppPluginsDirectory
			class OpenFoldersBootstrapOptionDirectory:
				ID = "OpenFoldersBootstrapOptionDirectory"
				Index = 12
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersBootstrapOptionDirectory = AllControls.OpenFoldersBootstrapOptionDirectory
			class OpenFoldersOptionsDirectory:
				ID = "OpenFoldersOptionsDirectory"
				Index = 13
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersOptionsDirectory = AllControls.OpenFoldersOptionsDirectory
			class OpenFoldersCloudCacheDirectory:
				ID = "OpenFoldersCloudCacheDirectory"
				Index = 14
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersCloudCacheDirectory = AllControls.OpenFoldersCloudCacheDirectory
			class OpenFoldersScriptsDirectory:
				ID = "OpenFoldersScriptsDirectory"
				Index = 15
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersScriptsDirectory = AllControls.OpenFoldersScriptsDirectory
			class OpenFoldersAutorunScriptsDirectory:
				ID = "OpenFoldersAutorunScriptsDirectory"
				Index = 16
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAutorunScriptsDirectory = AllControls.OpenFoldersAutorunScriptsDirectory
			class OpenFoldersSamplesScriptsDirectory:
				ID = "OpenFoldersSamplesScriptsDirectory"
				Index = 17
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersSamplesScriptsDirectory = AllControls.OpenFoldersSamplesScriptsDirectory
			class OpenFoldersProgramDataScriptsDirectory:
				ID = "OpenFoldersProgramDataScriptsDirectory"
				Index = 18
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersProgramDataScriptsDirectory = AllControls.OpenFoldersProgramDataScriptsDirectory
			class OpenFoldersAppDataScriptsDirectory:
				ID = "OpenFoldersAppDataScriptsDirectory"
				Index = 19
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAppDataScriptsDirectory = AllControls.OpenFoldersAppDataScriptsDirectory
			class OpenFoldersManuallyInstalledScriptsDirectory:
				ID = "OpenFoldersManuallyInstalledScriptsDirectory"
				Index = 20
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersManuallyInstalledScriptsDirectory = AllControls.OpenFoldersManuallyInstalledScriptsDirectory
			class OpenFoldersMaterialsDirectory:
				ID = "OpenFoldersMaterialsDirectory"
				Index = 21
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersMaterialsDirectory = AllControls.OpenFoldersMaterialsDirectory
			class OpenFoldersTestTempDirectory:
				ID = "OpenFoldersTestTempDirectory"
				Index = 22
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersTestTempDirectory = AllControls.OpenFoldersTestTempDirectory
			class OpenFoldersScratchDirectory:
				ID = "OpenFoldersScratchDirectory"
				Index = 23
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersScratchDirectory = AllControls.OpenFoldersScratchDirectory
			class OpenFoldersResultDirectory:
				ID = "OpenFoldersResultDirectory"
				Index = 24
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersResultDirectory = AllControls.OpenFoldersResultDirectory
			class OpenFoldersSampleDirectory:
				ID = "OpenFoldersSampleDirectory"
				Index = 25
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersSampleDirectory = AllControls.OpenFoldersSampleDirectory
			class OpenFoldersAppLogFilePath:
				ID = "OpenFoldersAppLogFilePath"
				Index = 26
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAppLogFilePath = AllControls.OpenFoldersAppLogFilePath
			class OpenFoldersCacheDirectory:
				ID = "OpenFoldersCacheDirectory"
				Index = 27
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersCacheDirectory = AllControls.OpenFoldersCacheDirectory
			class OpenFoldersAutoSaveDirectory:
				ID = "OpenFoldersAutoSaveDirectory"
				Index = 28
				isPromoted = False
				isPromotedByDefault = False
				OpenFoldersAutoSaveDirectory = AllControls.OpenFoldersAutoSaveDirectory
		class OpenFoldersseparatorBottom:
			ID = "OpenFoldersseparatorBottom"
			Index = 7
	class UtilityPanel:
		ID = "UtilityPanel"
		class MaterialCommand:
			ID = "MaterialCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MaterialCommand = AllControls.MaterialCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
	class SelectPanel:
		ID = "SelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SelectCommand = AllControls.SelectCommand
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			selectWindow = AllControls.selectWindow
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			selectFreeForm = AllControls.selectFreeForm
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			selectPaint = AllControls.selectPaint
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SelectionToolsDropDown:
			ID = "SelectionToolsDropDown"
			Index = 6
			class SelectByNameCommand:
				ID = "SelectByNameCommand"
				Index = 0
				SelectByNameCommand = AllControls.SelectByNameCommand
			class SelectByBoundaryCommand:
				ID = "SelectByBoundaryCommand"
				Index = 1
				SelectByBoundaryCommand = AllControls.SelectByBoundaryCommand
			class FusionSelectBodiesBySizeCommand:
				ID = "FusionSelectBodiesBySizeCommand"
				Index = 2
				FusionSelectBodiesBySizeCommand = AllControls.FusionSelectBodiesBySizeCommand
			class SelectByInvertCommand:
				ID = "SelectByInvertCommand"
				Index = 3
				SelectByInvertCommand = AllControls.SelectByInvertCommand
		class SeparatorAfter_SelectionToolsDropDown:
			ID = "SeparatorAfter_SelectionToolsDropDown"
			Index = 7
		class FusionDragCompControlsCmd:
			ID = "FusionDragCompControlsCmd"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			FusionDragCompControlsCmd = AllControls.FusionDragCompControlsCmd
		class thomasa88_NoComponentDrag_Enable:
			ID = "thomasa88_NoComponentDrag_Enable"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			thomasa88_NoComponentDrag_Enable = AllControls.thomasa88_NoComponentDrag_Enable
		class SeparatorAfter_FusionDragCompControlsCmd:
			ID = "SeparatorAfter_FusionDragCompControlsCmd"
			Index = 10
		class SelectionPriorityCommandsDropDown:
			ID = "SelectionPriorityCommandsDropDown"
			Index = 11
			class SelectBodyPriorityCommand:
				ID = "SelectBodyPriorityCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				SelectBodyPriorityCommand = AllControls.SelectBodyPriorityCommand
			class SelectFacePriorityCommand:
				ID = "SelectFacePriorityCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				SelectFacePriorityCommand = AllControls.SelectFacePriorityCommand
			class SelectEdgePriorityCommand:
				ID = "SelectEdgePriorityCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				SelectEdgePriorityCommand = AllControls.SelectEdgePriorityCommand
			class SelectComponentPriorityCommand:
				ID = "SelectComponentPriorityCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
				SelectComponentPriorityCommand = AllControls.SelectComponentPriorityCommand
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			SelectionFilterCommand = AllControls.SelectionFilterCommand
	class NewPanel:
		ID = "NewPanel"
		class NC1:
			ID = "NC1"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			NC1 = AllControls.NC1
		class NC4:
			ID = "NC4"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			NC4 = AllControls.NC4
		class NC8:
			ID = "NC8"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			NC8 = AllControls.NC8
		class NC7:
			ID = "NC7"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			NC7 = AllControls.NC7
		class NC11:
			ID = "NC11"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			NC11 = AllControls.NC11
		class uuid_c74c2f30_7c04_497b_aede_77a8a7f08e7d:
			ID = "c74c2f30-7c04-497b-aede-77a8a7f08e7d"
			Index = 5
		class NC2:
			ID = "NC2"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			NC2 = AllControls.NC2
		class NC3:
			ID = "NC3"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			NC3 = AllControls.NC3
		class NC6:
			ID = "NC6"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			NC6 = AllControls.NC6
		class NC5:
			ID = "NC5"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			NC5 = AllControls.NC5
		class uuid_01e827ff_84d8_4ebd_aa30_a1d98a55a3d2:
			ID = "01e827ff-84d8-4ebd-aa30-a1d98a55a3d2"
			Index = 10
		class NC9:
			ID = "NC9"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			NC9 = AllControls.NC9
		class NC10:
			ID = "NC10"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			NC10 = AllControls.NC10
	class MeshSelectPanel:
		ID = "MeshSelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SelectCommand = AllControls.SelectCommand
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			selectWindow = AllControls.selectWindow
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			selectFreeForm = AllControls.selectFreeForm
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			selectPaint = AllControls.selectPaint
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SeparatorAfter_SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_SeparatorAfter_selectPaint"
			Index = 6
		class FusionShowSelectionPanelCmd:
			ID = "FusionShowSelectionPanelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionShowSelectionPanelCmd = AllControls.FusionShowSelectionPanelCmd
		class SeparatorAfter_FusionShowSelectionPanelCmd:
			ID = "SeparatorAfter_FusionShowSelectionPanelCmd"
			Index = 8
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			SelectionFilterCommand = AllControls.SelectionFilterCommand
	class StopSketchPanel:
		ID = "StopSketchPanel"
		class SketchStop:
			ID = "SketchStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SketchStop = AllControls.SketchStop
	class StopBaseFeaturePanel:
		ID = "StopBaseFeaturePanel"
		class BaseFeatureStop:
			ID = "BaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			BaseFeatureStop = AllControls.BaseFeatureStop
	class StopTSplineBaseFeaturePanel:
		ID = "StopTSplineBaseFeaturePanel"
		class TSplineBaseFeatureStop:
			ID = "TSplineBaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			TSplineBaseFeatureStop = AllControls.TSplineBaseFeatureStop
	class StopMeshBaseFeaturePanel:
		ID = "StopMeshBaseFeaturePanel"
		class MeshBaseFeatureStop:
			ID = "MeshBaseFeatureStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			MeshBaseFeatureStop = AllControls.MeshBaseFeatureStop
	class SnapshotPanel:
		ID = "SnapshotPanel"
		class SnapshotCmd:
			ID = "SnapshotCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SnapshotCmd = AllControls.SnapshotCmd
		class AsBuiltPositionsCmd:
			ID = "AsBuiltPositionsCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			AsBuiltPositionsCmd = AllControls.AsBuiltPositionsCmd
	class FinishSnapshotEditPanel:
		ID = "FinishSnapshotEditPanel"
		class SnapshotEditAccept:
			ID = "SnapshotEditAccept"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SnapshotEditAccept = AllControls.SnapshotEditAccept
		class SnapshotEditCancel:
			ID = "SnapshotEditCancel"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			SnapshotEditCancel = AllControls.SnapshotEditCancel
	class SnapshotSolidModifyPanel:
		ID = "SnapshotSolidModifyPanel"
		class FusionPressPullCommand:
			ID = "FusionPressPullCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			FusionPressPullCommand = AllControls.FusionPressPullCommand
		class EditFaceCommand:
			ID = "EditFaceCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			EditFaceCommand = AllControls.EditFaceCommand
		class SeparatorAfter_EditFaceCommand:
			ID = "SeparatorAfter_EditFaceCommand"
			Index = 2
		class FusionFilletEdgesCommand:
			ID = "FusionFilletEdgesCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionFilletEdgesCommand = AllControls.FusionFilletEdgesCommand
		class FusionChamferCommand:
			ID = "FusionChamferCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionChamferCommand = AllControls.FusionChamferCommand
		class SeparatorAfter_FusionChamferCommand:
			ID = "SeparatorAfter_FusionChamferCommand"
			Index = 5
		class FusionShellBodyCommand:
			ID = "FusionShellBodyCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionShellBodyCommand = AllControls.FusionShellBodyCommand
		class FusionDraftCommand:
			ID = "FusionDraftCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionDraftCommand = AllControls.FusionDraftCommand
		class ModifyScale:
			ID = "ModifyScale"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			ModifyScale = AllControls.ModifyScale
		class FusionCombineCommand:
			ID = "FusionCombineCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionCombineCommand = AllControls.FusionCombineCommand
		class FusionReplaceFaceCommand:
			ID = "FusionReplaceFaceCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionReplaceFaceCommand = AllControls.FusionReplaceFaceCommand
		class FusionSplitFaceCommand:
			ID = "FusionSplitFaceCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionSplitFaceCommand = AllControls.FusionSplitFaceCommand
		class FusionSplitBodyCommand:
			ID = "FusionSplitBodyCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionSplitBodyCommand = AllControls.FusionSplitBodyCommand
		class FusionPartingLineSplitCmd:
			ID = "FusionPartingLineSplitCmd"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			FusionPartingLineSplitCmd = AllControls.FusionPartingLineSplitCmd
		class SeparatorAfter_FusionPartingLineSplitCmd:
			ID = "SeparatorAfter_FusionPartingLineSplitCmd"
			Index = 14
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 15
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class AlignCmd:
			ID = "AlignCmd"
			Index = 16
			isPromoted = True
			isPromotedByDefault = True
			AlignCmd = AllControls.AlignCmd
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 18
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 19
			isPromoted = False
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
		class SeparatorAfter_FusionComputeAllCommand:
			ID = "SeparatorAfter_FusionComputeAllCommand"
			Index = 21
		class TSpline2BRepCommand:
			ID = "TSpline2BRepCommand"
			Index = 22
			isPromoted = False
			isPromotedByDefault = False
			TSpline2BRepCommand = AllControls.TSpline2BRepCommand
		class MeshDropDown:
			ID = "MeshDropDown"
			Index = 23
			class Mesh2BRepCommand:
				ID = "Mesh2BRepCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				Mesh2BRepCommand = AllControls.Mesh2BRepCommand
			class BRep2MeshCommand:
				ID = "BRep2MeshCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				BRep2MeshCommand = AllControls.BRep2MeshCommand
	class SheetmetalRefoldPanel:
		ID = "SheetmetalRefoldPanel"
		class FusionSheetmetalRefoldCommand:
			ID = "FusionSheetmetalRefoldCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionSheetmetalRefoldCommand = AllControls.FusionSheetmetalRefoldCommand
	class StopPCBPanel:
		ID = "StopPCBPanel"
		class PCBStop:
			ID = "PCBStop"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PCBStop = AllControls.PCBStop
	class ReturnPanel:
		ID = "ReturnPanel"
		class ReturnToEnvironmentCommand:
			ID = "ReturnToEnvironmentCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ReturnToEnvironmentCommand = AllControls.ReturnToEnvironmentCommand
		class ReturnToExternalAppCmdDefINV:
			ID = "ReturnToExternalAppCmdDefINV"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			ReturnToExternalAppCmdDefINV = AllControls.ReturnToExternalAppCmdDefINV
		class ReturnToExternalAppCmdDefACAD:
			ID = "ReturnToExternalAppCmdDefACAD"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			ReturnToExternalAppCmdDefACAD = AllControls.ReturnToExternalAppCmdDefACAD
		class ReturnToExternalAppCmdDefMoldflow:
			ID = "ReturnToExternalAppCmdDefMoldflow"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ReturnToExternalAppCmdDefMoldflow = AllControls.ReturnToExternalAppCmdDefMoldflow
	class RenderSetupPanel:
		ID = "RenderSetupPanel"
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			AppearanceCommand = AllControls.AppearanceCommand
		class RenderingEnvCmd:
			ID = "RenderingEnvCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			RenderingEnvCmd = AllControls.RenderingEnvCmd
		class FusionAddEditDecalCommand:
			ID = "FusionAddEditDecalCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionAddEditDecalCommand = AllControls.FusionAddEditDecalCommand
		class TextureMappingCommand:
			ID = "TextureMappingCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			TextureMappingCommand = AllControls.TextureMappingCommand
	class InCanvasRenderPanel:
		ID = "InCanvasRenderPanel"
		class InCanvasRenderCommand:
			ID = "InCanvasRenderCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			InCanvasRenderCommand = AllControls.InCanvasRenderCommand
		class InCanvasRenderSettingsCommand:
			ID = "InCanvasRenderSettingsCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			InCanvasRenderSettingsCommand = AllControls.InCanvasRenderSettingsCommand
		class SaveAsImageCommand:
			ID = "SaveAsImageCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			SaveAsImageCommand = AllControls.SaveAsImageCommand
	class RenderPanel:
		ID = "RenderPanel"
		class A360RenderCommand:
			ID = "A360RenderCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			A360RenderCommand = AllControls.A360RenderCommand
	class ToolsPanel:
		ID = "ToolsPanel"
		class selectWindow:
			ID = "selectWindow"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			selectWindow = AllControls.selectWindow
	class AssignPanel:
		ID = "AssignPanel"
		class PIMAssignItemNumberCmd:
			ID = "PIMAssignItemNumberCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PIMAssignItemNumberCmd = AllControls.PIMAssignItemNumberCmd
	class ReleasePanel:
		ID = "ReleasePanel"
		class PIMQuickReleaseCmd:
			ID = "PIMQuickReleaseCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PIMQuickReleaseCmd = AllControls.PIMQuickReleaseCmd
		class PIMECOReleaseCmd:
			ID = "PIMECOReleaseCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PIMECOReleaseCmd = AllControls.PIMECOReleaseCmd
	class NESTPanel:
		ID = "NESTPanel"
		class MSFNestAuthoringCmd:
			ID = "MSFNestAuthoringCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = False
			MSFNestAuthoringCmd = AllControls.MSFNestAuthoringCmd
	class ParaMeshCreatePanel:
		ID = "ParaMeshCreatePanel"
		class ParaMeshInsertAlignCommand:
			ID = "ParaMeshInsertAlignCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshInsertAlignCommand = AllControls.ParaMeshInsertAlignCommand
		class ParaMeshTessellateCommand:
			ID = "ParaMeshTessellateCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshTessellateCommand = AllControls.ParaMeshTessellateCommand
		class SeparatorAfter_ParaMeshTessellateCommand:
			ID = "SeparatorAfter_ParaMeshTessellateCommand"
			Index = 2
		class ParaMeshPlanarSectionCommand:
			ID = "ParaMeshPlanarSectionCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshPlanarSectionCommand = AllControls.ParaMeshPlanarSectionCommand
	class ParaMeshPreparePanel:
		ID = "ParaMeshPreparePanel"
		class ParaMeshRepairCommand:
			ID = "ParaMeshRepairCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshRepairCommand = AllControls.ParaMeshRepairCommand
		class ParaMeshCalculateFaceGroupsCommand:
			ID = "ParaMeshCalculateFaceGroupsCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshCalculateFaceGroupsCommand = AllControls.ParaMeshCalculateFaceGroupsCommand
		class ParaMeshMergeFaceGroupsCommand:
			ID = "ParaMeshMergeFaceGroupsCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshMergeFaceGroupsCommand = AllControls.ParaMeshMergeFaceGroupsCommand
		class ParaMeshCreateFaceGroupCommand:
			ID = "ParaMeshCreateFaceGroupCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshCreateFaceGroupCommand = AllControls.ParaMeshCreateFaceGroupCommand
	class ParaMeshModifyPanel:
		ID = "ParaMeshModifyPanel"
		class ParaMeshBaseFeatureCreateCommand:
			ID = "ParaMeshBaseFeatureCreateCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshBaseFeatureCreateCommand = AllControls.ParaMeshBaseFeatureCreateCommand
		class ParaMeshRemeshCommand:
			ID = "ParaMeshRemeshCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshRemeshCommand = AllControls.ParaMeshRemeshCommand
		class ParaMeshReduceCommand:
			ID = "ParaMeshReduceCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshReduceCommand = AllControls.ParaMeshReduceCommand
		class ParaMeshPlaneCutCommand:
			ID = "ParaMeshPlaneCutCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshPlaneCutCommand = AllControls.ParaMeshPlaneCutCommand
		class ParaMeshHollowCommand:
			ID = "ParaMeshHollowCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshHollowCommand = AllControls.ParaMeshHollowCommand
		class ParaMeshCombineCommand:
			ID = "ParaMeshCombineCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshCombineCommand = AllControls.ParaMeshCombineCommand
		class ParaMeshSmoothCommand:
			ID = "ParaMeshSmoothCommand"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshSmoothCommand = AllControls.ParaMeshSmoothCommand
		class ParaMeshReverseNormalsCommand:
			ID = "ParaMeshReverseNormalsCommand"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshReverseNormalsCommand = AllControls.ParaMeshReverseNormalsCommand
		class ParaMeshEraseAndFillCommand:
			ID = "ParaMeshEraseAndFillCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshEraseAndFillCommand = AllControls.ParaMeshEraseAndFillCommand
		class SeparatorAfter_ParaMeshEraseAndFillCommand:
			ID = "SeparatorAfter_ParaMeshEraseAndFillCommand"
			Index = 9
		class ParaMeshExtractCommand:
			ID = "ParaMeshExtractCommand"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshExtractCommand = AllControls.ParaMeshExtractCommand
		class SeparatorAfter_ParaMeshExtractCommand:
			ID = "SeparatorAfter_ParaMeshExtractCommand"
			Index = 11
		class FusionMoveCommand:
			ID = "FusionMoveCommand"
			Index = 12
			isPromoted = True
			isPromotedByDefault = True
			FusionMoveCommand = AllControls.FusionMoveCommand
		class ParaMeshScaleCommand:
			ID = "ParaMeshScaleCommand"
			Index = 13
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshScaleCommand = AllControls.ParaMeshScaleCommand
		class FusionDeleteCommand:
			ID = "FusionDeleteCommand"
			Index = 14
			isPromoted = False
			isPromotedByDefault = False
			FusionDeleteCommand = AllControls.FusionDeleteCommand
		class SeparatorAfter_FusionDeleteCommand:
			ID = "SeparatorAfter_FusionDeleteCommand"
			Index = 15
		class ParaMeshConvertCommand:
			ID = "ParaMeshConvertCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshConvertCommand = AllControls.ParaMeshConvertCommand
		class ParaMeshLatticeCommand:
			ID = "ParaMeshLatticeCommand"
			Index = 17
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshLatticeCommand = AllControls.ParaMeshLatticeCommand
		class ParaMeshToQuadMeshCommand:
			ID = "ParaMeshToQuadMeshCommand"
			Index = 18
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshToQuadMeshCommand = AllControls.ParaMeshToQuadMeshCommand
		class SeparatorAfter_ParaMeshToQuadMeshCommand:
			ID = "SeparatorAfter_ParaMeshToQuadMeshCommand"
			Index = 19
		class PhysicalMaterialCommand:
			ID = "PhysicalMaterialCommand"
			Index = 20
			isPromoted = False
			isPromotedByDefault = False
			PhysicalMaterialCommand = AllControls.PhysicalMaterialCommand
		class AppearanceCommand:
			ID = "AppearanceCommand"
			Index = 21
			isPromoted = False
			isPromotedByDefault = False
			AppearanceCommand = AllControls.AppearanceCommand
		class SeparatorAfter_AppearanceCommand:
			ID = "SeparatorAfter_AppearanceCommand"
			Index = 22
		class ChangeParameterCommand:
			ID = "ChangeParameterCommand"
			Index = 23
			isPromoted = False
			isPromotedByDefault = False
			ChangeParameterCommand = AllControls.ChangeParameterCommand
		class FusionComputeAllCommand:
			ID = "FusionComputeAllCommand"
			Index = 24
			isPromoted = False
			isPromotedByDefault = False
			FusionComputeAllCommand = AllControls.FusionComputeAllCommand
	class ParaMeshSelectPanel:
		ID = "ParaMeshSelectPanel"
		class SelectCommand:
			ID = "SelectCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			SelectCommand = AllControls.SelectCommand
		class SeparatorAfter_SelectCommand:
			ID = "SeparatorAfter_SelectCommand"
			Index = 1
		class selectWindow:
			ID = "selectWindow"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			selectWindow = AllControls.selectWindow
		class selectFreeForm:
			ID = "selectFreeForm"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			selectFreeForm = AllControls.selectFreeForm
		class selectPaint:
			ID = "selectPaint"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			selectPaint = AllControls.selectPaint
		class SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_selectPaint"
			Index = 5
		class SeparatorAfter_SeparatorAfter_selectPaint:
			ID = "SeparatorAfter_SeparatorAfter_selectPaint"
			Index = 6
		class ParaMeshShowSelectionPanelCmd:
			ID = "ParaMeshShowSelectionPanelCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			ParaMeshShowSelectionPanelCmd = AllControls.ParaMeshShowSelectionPanelCmd
		class SeparatorAfter_ParaMeshShowSelectionPanelCmd:
			ID = "SeparatorAfter_ParaMeshShowSelectionPanelCmd"
			Index = 8
		class SelectionFilterCommand:
			ID = "SelectionFilterCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			SelectionFilterCommand = AllControls.SelectionFilterCommand
	class ParaMeshExportPanel:
		ID = "ParaMeshExportPanel"
		class ParaMeshExportCommand:
			ID = "ParaMeshExportCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshExportCommand = AllControls.ParaMeshExportCommand
		class ThreeDprintCmdDef:
			ID = "ThreeDprintCmdDef"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			ThreeDprintCmdDef = AllControls.ThreeDprintCmdDef
	class ParaMeshBaseFeatureStopPanel:
		ID = "ParaMeshBaseFeatureStopPanel"
		class ParaMeshBaseFeatureStopCommand:
			ID = "ParaMeshBaseFeatureStopCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			ParaMeshBaseFeatureStopCommand = AllControls.ParaMeshBaseFeatureStopCommand
	class thomasa88_anyShortcutPanel:
		ID = "thomasa88_anyShortcutPanel"
		class thomasa88_anyShortcutPremadeDropdown:
			ID = "thomasa88_anyShortcutPremadeDropdown"
			Index = 0
			class thomasa88_anyShortcutListLookAtSketchCommand:
				ID = "thomasa88_anyShortcutListLookAtSketchCommand"
				Index = 0
				isPromoted = False
				isPromotedByDefault = False
				thomasa88_anyShortcutListLookAtSketchCommand = AllControls.thomasa88_anyShortcutListLookAtSketchCommand
			class thomasa88_anyShortcutListLookAtSketchOrSelectedCommand:
				ID = "thomasa88_anyShortcutListLookAtSketchOrSelectedCommand"
				Index = 1
				isPromoted = False
				isPromotedByDefault = False
				thomasa88_anyShortcutListLookAtSketchOrSelectedCommand = AllControls.thomasa88_anyShortcutListLookAtSketchOrSelectedCommand
			class thomasa88_anyShortcutListActivateContainingOrComponentCommand:
				ID = "thomasa88_anyShortcutListActivateContainingOrComponentCommand"
				Index = 2
				isPromoted = False
				isPromotedByDefault = False
				thomasa88_anyShortcutListActivateContainingOrComponentCommand = AllControls.thomasa88_anyShortcutListActivateContainingOrComponentCommand
			class thomasa88_anyShortcutBuiltinRepeatCommand:
				ID = "thomasa88_anyShortcutBuiltinRepeatCommand"
				Index = 3
				isPromoted = False
				isPromotedByDefault = False
				thomasa88_anyShortcutBuiltinRepeatCommand = AllControls.thomasa88_anyShortcutBuiltinRepeatCommand
			class thomasa88_anyShortcutBuiltinTimelineList:
				ID = "thomasa88_anyShortcutBuiltinTimelineList"
				Index = 4
				class thomasa88_anyShortcutListRollToBeginning:
					ID = "thomasa88_anyShortcutListRollToBeginning"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutListRollToBeginning = AllControls.thomasa88_anyShortcutListRollToBeginning
				class thomasa88_anyShortcutListRollBack:
					ID = "thomasa88_anyShortcutListRollBack"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutListRollBack = AllControls.thomasa88_anyShortcutListRollBack
				class thomasa88_anyShortcutListRollForward:
					ID = "thomasa88_anyShortcutListRollForward"
					Index = 2
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutListRollForward = AllControls.thomasa88_anyShortcutListRollForward
				class thomasa88_anyShortcutListRollToEnd:
					ID = "thomasa88_anyShortcutListRollToEnd"
					Index = 3
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutListRollToEnd = AllControls.thomasa88_anyShortcutListRollToEnd
			class thomasa88_anyShortcutBuiltinViewList:
				ID = "thomasa88_anyShortcutBuiltinViewList"
				Index = 5
				class thomasa88_anyShortcutBuiltinViewFront:
					ID = "thomasa88_anyShortcutBuiltinViewFront"
					Index = 0
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewFront = AllControls.thomasa88_anyShortcutBuiltinViewFront
				class thomasa88_anyShortcutBuiltinViewBack:
					ID = "thomasa88_anyShortcutBuiltinViewBack"
					Index = 1
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewBack = AllControls.thomasa88_anyShortcutBuiltinViewBack
				class thomasa88_anyShortcutBuiltinViewTop:
					ID = "thomasa88_anyShortcutBuiltinViewTop"
					Index = 2
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewTop = AllControls.thomasa88_anyShortcutBuiltinViewTop
				class thomasa88_anyShortcutBuiltinViewBottom:
					ID = "thomasa88_anyShortcutBuiltinViewBottom"
					Index = 3
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewBottom = AllControls.thomasa88_anyShortcutBuiltinViewBottom
				class thomasa88_anyShortcutBuiltinViewLeft:
					ID = "thomasa88_anyShortcutBuiltinViewLeft"
					Index = 4
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewLeft = AllControls.thomasa88_anyShortcutBuiltinViewLeft
				class thomasa88_anyShortcutBuiltinViewRight:
					ID = "thomasa88_anyShortcutBuiltinViewRight"
					Index = 5
					isPromoted = False
					isPromotedByDefault = False
					thomasa88_anyShortcutBuiltinViewRight = AllControls.thomasa88_anyShortcutBuiltinViewRight
		class thomasa88_anyShortcutDropdown:
			ID = "thomasa88_anyShortcutDropdown"
			Index = 1
			class thomasa88_anyShortcutList:
				ID = "thomasa88_anyShortcutList"
				Index = 0
				isPromoted = True
				isPromotedByDefault = True
				thomasa88_anyShortcutList = AllControls.thomasa88_anyShortcutList
			class uuid_e1fcc117_f6cd_4b6f_9441_a204364b6598:
				ID = "e1fcc117-f6cd-4b6f-9441-a204364b6598"
				Index = 1
	class PolyhedraGenerator:
		ID = "PolyhedraGenerator"
		class cmdID_PolyhedaCommand:
			ID = "cmdID_PolyhedaCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			cmdID_PolyhedaCommand = AllControls.cmdID_PolyhedaCommand
	class HexNutGenerator:
		ID = "HexNut Generator"
		class cmdID_HexNut:
			ID = "cmdID_HexNut"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			cmdID_HexNut = AllControls.cmdID_HexNut
	class ViewsPanel:
		ID = "ViewsPanel"
		class FusionDrawingViewBaseCommand:
			ID = "FusionDrawingViewBaseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewBaseCommand = AllControls.FusionDrawingViewBaseCommand
		class FusionDrawingViewBaseTemplateCommand:
			ID = "FusionDrawingViewBaseTemplateCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewBaseTemplateCommand = AllControls.FusionDrawingViewBaseTemplateCommand
		class FusionDrawingViewProjectCommand:
			ID = "FusionDrawingViewProjectCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewProjectCommand = AllControls.FusionDrawingViewProjectCommand
		class FusionDrawingViewProjectTemplateCommand:
			ID = "FusionDrawingViewProjectTemplateCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewProjectTemplateCommand = AllControls.FusionDrawingViewProjectTemplateCommand
		class FusionDrawingViewSimpleSectionCommand:
			ID = "FusionDrawingViewSimpleSectionCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewSimpleSectionCommand = AllControls.FusionDrawingViewSimpleSectionCommand
		class FusionDrawingViewSectionCommand:
			ID = "FusionDrawingViewSectionCommand"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewSectionCommand = AllControls.FusionDrawingViewSectionCommand
		class FusionDrawingViewDetailCommand:
			ID = "FusionDrawingViewDetailCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingViewDetailCommand = AllControls.FusionDrawingViewDetailCommand
		class SeparatorAfter_FusionDrawingViewDetailCommand:
			ID = "SeparatorAfter_FusionDrawingViewDetailCommand"
			Index = 7
		class FusionBrokenViewCommand:
			ID = "FusionBrokenViewCommand"
			Index = 8
			isPromoted = True
			isPromotedByDefault = True
			FusionBrokenViewCommand = AllControls.FusionBrokenViewCommand
		class SeparatorAfter_FusionBrokenViewCommand:
			ID = "SeparatorAfter_FusionBrokenViewCommand"
			Index = 9
		class FusionDrawingSketchCommand:
			ID = "FusionDrawingSketchCommand"
			Index = 10
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingSketchCommand = AllControls.FusionDrawingSketchCommand
	class DrawingPanel:
		ID = "DrawingPanel"
		class FusionDrawingLineCommand:
			ID = "FusionDrawingLineCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingLineCommand = AllControls.FusionDrawingLineCommand
		class FusionDrawingRectangleCommand:
			ID = "FusionDrawingRectangleCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingRectangleCommand = AllControls.FusionDrawingRectangleCommand
		class FusionDrawingCircleCommand:
			ID = "FusionDrawingCircleCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingCircleCommand = AllControls.FusionDrawingCircleCommand
		class FusionDrawingArcCommand:
			ID = "FusionDrawingArcCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingArcCommand = AllControls.FusionDrawingArcCommand
		class FusionDrawingArrowCommand:
			ID = "FusionDrawingArrowCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingArrowCommand = AllControls.FusionDrawingArrowCommand
	class ModifyPanel:
		ID = "ModifyPanel"
		class FusionDrawingMoveCmd:
			ID = "FusionDrawingMoveCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingMoveCmd = AllControls.FusionDrawingMoveCmd
		class FusionDocRotateCmd:
			ID = "FusionDocRotateCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDocRotateCmd = AllControls.FusionDocRotateCmd
		class FusionDrawingCopyCommand:
			ID = "FusionDrawingCopyCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingCopyCommand = AllControls.FusionDrawingCopyCommand
		class FusionDrawingTrimCommand:
			ID = "FusionDrawingTrimCommand"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingTrimCommand = AllControls.FusionDrawingTrimCommand
		class FusionDrawingExtendCommand:
			ID = "FusionDrawingExtendCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingExtendCommand = AllControls.FusionDrawingExtendCommand
		class FusionDrawingOffsetCommand:
			ID = "FusionDrawingOffsetCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingOffsetCommand = AllControls.FusionDrawingOffsetCommand
		class FusionDrawingEraseCmd:
			ID = "FusionDrawingEraseCmd"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingEraseCmd = AllControls.FusionDrawingEraseCmd
	class GeometryPanel:
		ID = "GeometryPanel"
		class FusionDrawingCenterlineCommand:
			ID = "FusionDrawingCenterlineCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingCenterlineCommand = AllControls.FusionDrawingCenterlineCommand
		class FusionDrawingCentermarkCommand:
			ID = "FusionDrawingCentermarkCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingCentermarkCommand = AllControls.FusionDrawingCentermarkCommand
		class FusionDrawingCenterPatternCommand:
			ID = "FusionDrawingCenterPatternCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingCenterPatternCommand = AllControls.FusionDrawingCenterPatternCommand
		class SeparatorAfter_FusionDrawingCenterPatternCommand:
			ID = "SeparatorAfter_FusionDrawingCenterPatternCommand"
			Index = 3
		class FusionDrawingEdgeExtensionCmd:
			ID = "FusionDrawingEdgeExtensionCmd"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingEdgeExtensionCmd = AllControls.FusionDrawingEdgeExtensionCmd
	class DimensionsPanel:
		ID = "DimensionsPanel"
		class FusionDrawingSingleDimensionCmd:
			ID = "FusionDrawingSingleDimensionCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingSingleDimensionCmd = AllControls.FusionDrawingSingleDimensionCmd
		class FusionDrawingOrdinateDimensionCmd:
			ID = "FusionDrawingOrdinateDimensionCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingOrdinateDimensionCmd = AllControls.FusionDrawingOrdinateDimensionCmd
		class SeparatorAfter_FusionDrawingOrdinateDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingOrdinateDimensionCmd"
			Index = 2
		class FusionDrawingLinearDimensionCmd:
			ID = "FusionDrawingLinearDimensionCmd"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingLinearDimensionCmd = AllControls.FusionDrawingLinearDimensionCmd
		class FusionDrawingAlignedDimensionCmd:
			ID = "FusionDrawingAlignedDimensionCmd"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingAlignedDimensionCmd = AllControls.FusionDrawingAlignedDimensionCmd
		class FusionDrawingAngularDimensionCmd:
			ID = "FusionDrawingAngularDimensionCmd"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingAngularDimensionCmd = AllControls.FusionDrawingAngularDimensionCmd
		class FusionDrawingRadialDimensionCmd:
			ID = "FusionDrawingRadialDimensionCmd"
			Index = 6
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingRadialDimensionCmd = AllControls.FusionDrawingRadialDimensionCmd
		class FusionDrawingDiameterDimensionCmd:
			ID = "FusionDrawingDiameterDimensionCmd"
			Index = 7
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingDiameterDimensionCmd = AllControls.FusionDrawingDiameterDimensionCmd
		class SeparatorAfter_FusionDrawingDiameterDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingDiameterDimensionCmd"
			Index = 8
		class FusionDrawingBaselineDimensionCmd:
			ID = "FusionDrawingBaselineDimensionCmd"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingBaselineDimensionCmd = AllControls.FusionDrawingBaselineDimensionCmd
		class FusionDrawingChainDimensionCmd:
			ID = "FusionDrawingChainDimensionCmd"
			Index = 10
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingChainDimensionCmd = AllControls.FusionDrawingChainDimensionCmd
		class SeparatorAfter_FusionDrawingChainDimensionCmd:
			ID = "SeparatorAfter_FusionDrawingChainDimensionCmd"
			Index = 11
		class FusionDrawingDimensionBreakCmd:
			ID = "FusionDrawingDimensionBreakCmd"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingDimensionBreakCmd = AllControls.FusionDrawingDimensionBreakCmd
	class TextPanel:
		ID = "TextPanel"
		class FusionDrawingMTextCommand:
			ID = "FusionDrawingMTextCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingMTextCommand = AllControls.FusionDrawingMTextCommand
		class SeparatorAfter_FusionDrawingMTextCommand:
			ID = "SeparatorAfter_FusionDrawingMTextCommand"
			Index = 1
		class FusionDrawingNoteCommand:
			ID = "FusionDrawingNoteCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingNoteCommand = AllControls.FusionDrawingNoteCommand
		class FusionDrawingLeaderCommand:
			ID = "FusionDrawingLeaderCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingLeaderCommand = AllControls.FusionDrawingLeaderCommand
		class FusionDrawingHoleThreadNoteLeaderCommand:
			ID = "FusionDrawingHoleThreadNoteLeaderCommand"
			Index = 4
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingHoleThreadNoteLeaderCommand = AllControls.FusionDrawingHoleThreadNoteLeaderCommand
		class FusionDrawingBendNoteLeaderCommand:
			ID = "FusionDrawingBendNoteLeaderCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingBendNoteLeaderCommand = AllControls.FusionDrawingBendNoteLeaderCommand
		class FusionDrawingAttDefCommand:
			ID = "FusionDrawingAttDefCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingAttDefCommand = AllControls.FusionDrawingAttDefCommand
	class InspectPanel:
		ID = "InspectPanel"
		class FusionDrawingMeasureCommand:
			ID = "FusionDrawingMeasureCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingMeasureCommand = AllControls.FusionDrawingMeasureCommand
	class SymbolsPanel:
		ID = "SymbolsPanel"
		class FusionDrawingSurfaceTextureCmd:
			ID = "FusionDrawingSurfaceTextureCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingSurfaceTextureCmd = AllControls.FusionDrawingSurfaceTextureCmd
		class SeparatorAfter_FusionDrawingSurfaceTextureCmd:
			ID = "SeparatorAfter_FusionDrawingSurfaceTextureCmd"
			Index = 1
		class FusionDrawingFeatureControlFrameCmd:
			ID = "FusionDrawingFeatureControlFrameCmd"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingFeatureControlFrameCmd = AllControls.FusionDrawingFeatureControlFrameCmd
		class FusionDrawingDatumIdCmd:
			ID = "FusionDrawingDatumIdCmd"
			Index = 3
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingDatumIdCmd = AllControls.FusionDrawingDatumIdCmd
		class SeparatorAfter_FusionDrawingDatumIdCmd:
			ID = "SeparatorAfter_FusionDrawingDatumIdCmd"
			Index = 4
		class FusionDrawingWeldSymbolCmd:
			ID = "FusionDrawingWeldSymbolCmd"
			Index = 5
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingWeldSymbolCmd = AllControls.FusionDrawingWeldSymbolCmd
		class FusionDrawingTaperSlopeSymbolCmd:
			ID = "FusionDrawingTaperSlopeSymbolCmd"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingTaperSlopeSymbolCmd = AllControls.FusionDrawingTaperSlopeSymbolCmd
	class InsertPanel:
		ID = "InsertPanel"
		class FusionDrawingImageInsertCommand:
			ID = "FusionDrawingImageInsertCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingImageInsertCommand = AllControls.FusionDrawingImageInsertCommand
		class FusionDrawingBlockEditorImageInsertCommand:
			ID = "FusionDrawingBlockEditorImageInsertCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBlockEditorImageInsertCommand = AllControls.FusionDrawingBlockEditorImageInsertCommand
		class FusionDrawingTemplateImageInsertCommand:
			ID = "FusionDrawingTemplateImageInsertCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingTemplateImageInsertCommand = AllControls.FusionDrawingTemplateImageInsertCommand
	class BillOfMaterialsPanel:
		ID = "BillOfMaterialsPanel"
		class FusionDrawingCreatePartsListCommand:
			ID = "FusionDrawingCreatePartsListCommand"
			Index = 0
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingCreatePartsListCommand = AllControls.FusionDrawingCreatePartsListCommand
		class FusionDrawingNewTableCommand:
			ID = "FusionDrawingNewTableCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingNewTableCommand = AllControls.FusionDrawingNewTableCommand
		class FusionDrawingNewTableTemplateCommand:
			ID = "FusionDrawingNewTableTemplateCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingNewTableTemplateCommand = AllControls.FusionDrawingNewTableTemplateCommand
		class FusionDrawingEmptyTableCommand:
			ID = "FusionDrawingEmptyTableCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingEmptyTableCommand = AllControls.FusionDrawingEmptyTableCommand
		class SeparatorAfter_FusionDrawingEmptyTableCommand:
			ID = "SeparatorAfter_FusionDrawingEmptyTableCommand"
			Index = 4
		class FusionDrawingPartsListTableCommand:
			ID = "FusionDrawingPartsListTableCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingPartsListTableCommand = AllControls.FusionDrawingPartsListTableCommand
		class FusionDrawingBalloonCommand:
			ID = "FusionDrawingBalloonCommand"
			Index = 6
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBalloonCommand = AllControls.FusionDrawingBalloonCommand
		class SeparatorAfter_FusionDrawingBalloonCommand:
			ID = "SeparatorAfter_FusionDrawingBalloonCommand"
			Index = 7
		class FusionDrawingBendTableCommand:
			ID = "FusionDrawingBendTableCommand"
			Index = 8
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingBendTableCommand = AllControls.FusionDrawingBendTableCommand
		class FusionDrawingBendIDCommand:
			ID = "FusionDrawingBendIDCommand"
			Index = 9
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingBendIDCommand = AllControls.FusionDrawingBendIDCommand
		class SeparatorAfter_FusionDrawingBendIDCommand:
			ID = "SeparatorAfter_FusionDrawingBendIDCommand"
			Index = 10
		class FusionDrawingRevisionTableCommand:
			ID = "FusionDrawingRevisionTableCommand"
			Index = 11
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingRevisionTableCommand = AllControls.FusionDrawingRevisionTableCommand
		class FusionDrawingRevMarkerCommand:
			ID = "FusionDrawingRevMarkerCommand"
			Index = 12
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingRevMarkerCommand = AllControls.FusionDrawingRevMarkerCommand
		class FusionDocRevCloudCommand:
			ID = "FusionDocRevCloudCommand"
			Index = 13
			isPromoted = False
			isPromotedByDefault = False
			FusionDocRevCloudCommand = AllControls.FusionDocRevCloudCommand
		class SeparatorAfter_FusionDocRevCloudCommand:
			ID = "SeparatorAfter_FusionDocRevCloudCommand"
			Index = 14
		class FusionDrawingRenumberCommand:
			ID = "FusionDrawingRenumberCommand"
			Index = 15
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingRenumberCommand = AllControls.FusionDrawingRenumberCommand
		class FusionDrawingAlignBalloonCommand:
			ID = "FusionDrawingAlignBalloonCommand"
			Index = 16
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingAlignBalloonCommand = AllControls.FusionDrawingAlignBalloonCommand
	class BlockPanel:
		ID = "BlockPanel"
		class FusionDrawingBlockCloseCommand:
			ID = "FusionDrawingBlockCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBlockCloseCommand = AllControls.FusionDrawingBlockCloseCommand
		class FusionDrawingBorderCloseCommand:
			ID = "FusionDrawingBorderCloseCommand"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBorderCloseCommand = AllControls.FusionDrawingBorderCloseCommand
		class FusionDrawingSketchCloseCommand:
			ID = "FusionDrawingSketchCloseCommand"
			Index = 2
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingSketchCloseCommand = AllControls.FusionDrawingSketchCloseCommand
	class StopBlockEditPanel:
		ID = "StopBlockEditPanel"
		class FusionDrawingBlockCloseCommand:
			ID = "FusionDrawingBlockCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBlockCloseCommand = AllControls.FusionDrawingBlockCloseCommand
	class StopBorderEditPanel:
		ID = "StopBorderEditPanel"
		class FusionDrawingBorderCloseCommand:
			ID = "FusionDrawingBorderCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingBorderCloseCommand = AllControls.FusionDrawingBorderCloseCommand
	class StopSketchEditPanel:
		ID = "StopSketchEditPanel"
		class FusionDrawingSketchCloseCommand:
			ID = "FusionDrawingSketchCloseCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingSketchCloseCommand = AllControls.FusionDrawingSketchCloseCommand
	class OutputPanel:
		ID = "OutputPanel"
		class FusionDrawingExportPDFCommand:
			ID = "FusionDrawingExportPDFCommand"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			FusionDrawingExportPDFCommand = AllControls.FusionDrawingExportPDFCommand
		class ExportFusionDrawingDocumentCommand:
			ID = "ExportFusionDrawingDocumentCommand"
			Index = 1
			isPromoted = False
			isPromotedByDefault = False
			ExportFusionDrawingDocumentCommand = AllControls.ExportFusionDrawingDocumentCommand
		class FusionDrawingExportDXFCommand:
			ID = "FusionDrawingExportDXFCommand"
			Index = 2
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingExportDXFCommand = AllControls.FusionDrawingExportDXFCommand
		class ExportFusionDrawingTemplateCommand:
			ID = "ExportFusionDrawingTemplateCommand"
			Index = 3
			isPromoted = False
			isPromotedByDefault = False
			ExportFusionDrawingTemplateCommand = AllControls.ExportFusionDrawingTemplateCommand
		class FusionDrawingExportPartsListCommand:
			ID = "FusionDrawingExportPartsListCommand"
			Index = 4
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingExportPartsListCommand = AllControls.FusionDrawingExportPartsListCommand
		class FusionDrawingDebugCommand:
			ID = "FusionDrawingDebugCommand"
			Index = 5
			isPromoted = False
			isPromotedByDefault = False
			FusionDrawingDebugCommand = AllControls.FusionDrawingDebugCommand
	class AssignPanel:
		ID = "AssignPanel"
		class PIMAssignItemNumberCmd:
			ID = "PIMAssignItemNumberCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PIMAssignItemNumberCmd = AllControls.PIMAssignItemNumberCmd
	class ReleasePanel:
		ID = "ReleasePanel"
		class PIMQuickReleaseCmd:
			ID = "PIMQuickReleaseCmd"
			Index = 0
			isPromoted = True
			isPromotedByDefault = True
			PIMQuickReleaseCmd = AllControls.PIMQuickReleaseCmd
		class PIMECOReleaseCmd:
			ID = "PIMECOReleaseCmd"
			Index = 1
			isPromoted = True
			isPromotedByDefault = True
			PIMECOReleaseCmd = AllControls.PIMECOReleaseCmd
class AllTabs:
	class MillingTab:
		ID = "MillingTab"
		class CAMJobPanel(AllPanels.CAMJobPanel):
			Index = 0
		class CAM2DPanel(AllPanels.CAM2DPanel):
			Index = 4
		class CAM3DPanel(AllPanels.CAM3DPanel):
			Index = 5
		class CAMDrillingPanel(AllPanels.CAMDrillingPanel):
			Index = 7
		class CAMMultiAxisPanel(AllPanels.CAMMultiAxisPanel):
			Index = 8
		class CAMDEDPanel(AllPanels.CAMDEDPanel):
			Index = 13
		class CAMEditPanel(AllPanels.CAMEditPanel):
			Index = 6
		class CAMActionPanel(AllPanels.CAMActionPanel):
			Index = 30
		class CAMManagePanel(AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class TurningTab:
		ID = "TurningTab"
		class CAMJobPanel(AllPanels.CAMJobPanel):
			Index = 0
		class CAMTurningPanel(AllPanels.CAMTurningPanel):
			Index = 9
		class CAMDrillingPanel(AllPanels.CAMDrillingPanel):
			Index = 7
		class CAMActionPanel(AllPanels.CAMActionPanel):
			Index = 30
		class CAMManagePanel(AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class AdditiveTab:
		ID = "AdditiveTab"
		class CAMAdditiveJobPanel(AllPanels.CAMAdditiveJobPanel):
			Index = 2
		class CAMAdditivePositioningPanel(AllPanels.CAMAdditivePositioningPanel):
			Index = 3
		class CAMAdditivePrintProfilePanel(AllPanels.CAMAdditivePrintProfilePanel):
			Index = 32
		class CAMInfillPanel(AllPanels.CAMInfillPanel):
			Index = 11
		class CAMSupportsPanel(AllPanels.CAMSupportsPanel):
			Index = 12
		class CAMDEDPanel(AllPanels.CAMDEDPanel):
			Index = 13
		class CAMEditPanel(AllPanels.CAMEditPanel):
			Index = 6
		class CAMAdditiveProcessSimPanel(AllPanels.CAMAdditiveProcessSimPanel):
			Index = 14
		class CAMAdditiveActionPanel(AllPanels.CAMAdditiveActionPanel):
			Index = 33
		class CAMAdditiveManagePanel(AllPanels.CAMAdditiveManagePanel):
			Index = 36
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class AdditiveResultsTab:
		ID = "AdditiveResultsTab"
		class CAMAdditiveProcessSimResultsPanel(AllPanels.CAMAdditiveProcessSimResultsPanel):
			Index = 15
		class CAMAdditiveProcessSimActionPanel(AllPanels.CAMAdditiveProcessSimActionPanel):
			Index = 16
		class CAMAdditiveProcessSimFinishPanel(AllPanels.CAMAdditiveProcessSimFinishPanel):
			Index = 17
	class ProbingTab:
		ID = "ProbingTab"
		class CAMJobPanel(AllPanels.CAMJobPanel):
			Index = 0
		class CAMProbingPanel(AllPanels.CAMProbingPanel):
			Index = 18
		class CAMCMMPanel(AllPanels.CAMCMMPanel):
			Index = 19
		class CAMManualInspectionPanel(AllPanels.CAMManualInspectionPanel):
			Index = 20
		class CAMProbingActionPanel(AllPanels.CAMProbingActionPanel):
			Index = 31
		class CAMManagePanel(AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class FabricationTab:
		ID = "FabricationTab"
		class ManufacturingSourcesPanel(AllPanels.ManufacturingSourcesPanel):
			Index = 40
		class NESTPanel(AllPanels.NESTPanel):
			Index = 43
		class CAMJobPanel(AllPanels.CAMJobPanel):
			Index = 0
		class CAMWLPCPanel(AllPanels.CAMWLPCPanel):
			Index = 10
		class CAMActionPanel(AllPanels.CAMActionPanel):
			Index = 30
		class FabricationManagePanel(AllPanels.FabricationManagePanel):
			Index = 41
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class UtilitiesTab:
		ID = "UtilitiesTab"
		class CAMInProcessStockPanel(AllPanels.CAMInProcessStockPanel):
			Index = 1
		class CAMManagePanel(AllPanels.CAMManagePanel):
			Index = 35
		class CAMInspectPanel(AllPanels.CAMInspectPanel):
			Index = 34
		class CAMScriptsAddinsPanel(AllPanels.CAMScriptsAddinsPanel):
			Index = 38
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
		class MachineBuilderActivationPanel(AllPanels.MachineBuilderActivationPanel):
			Index = 42
	class PartAlignmentTab:
		ID = "PartAlignmentTab"
		class CAMPartAlignmentEditPanel(AllPanels.CAMPartAlignmentEditPanel):
			Index = 21
		class CAMPartAlignmentInspectPanel(AllPanels.CAMPartAlignmentInspectPanel):
			Index = 22
		class CAMPartAlignmentPostPanel(AllPanels.CAMPartAlignmentPostPanel):
			Index = 23
		class CAMPartAlignmentResultsPanel(AllPanels.CAMPartAlignmentResultsPanel):
			Index = 25
		class CAMPartAlignmentPostAndExitPanel(AllPanels.CAMPartAlignmentPostAndExitPanel):
			Index = 27
		class CAMPartAlignmentFinishPanel(AllPanels.CAMPartAlignmentFinishPanel):
			Index = 28
	class LiveAlignmentTab:
		ID = "LiveAlignmentTab"
		class CAMPartAlignmentEditPanel(AllPanels.CAMPartAlignmentEditPanel):
			Index = 21
		class CAMPartAlignmentInspectPanel(AllPanels.CAMPartAlignmentInspectPanel):
			Index = 22
		class CAMLiveAlignmentPostPanel(AllPanels.CAMLiveAlignmentPostPanel):
			Index = 24
		class CAMLiveAlignmentResultsPanel(AllPanels.CAMLiveAlignmentResultsPanel):
			Index = 26
		class CAMLiveAlignmentFinishPanel(AllPanels.CAMLiveAlignmentFinishPanel):
			Index = 29
	class FeaturesTab:
		ID = "FeaturesTab"
		class CAMGeometryFeatures(AllPanels.CAMGeometryFeatures):
			Index = 37
		class SelectPanel(AllPanels.SelectPanel):
			Index = 39
	class MfgSolidTab:
		ID = "MfgSolidTab"
		class WMDComponentsManagerPanel(AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 4
		class GeneratePanel(AllPanels.GeneratePanel):
			Index = 5
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 6
		class WMDComponentsPanel(AllPanels.WMDComponentsPanel):
			Index = 46
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel(AllPanels.FinishPreparePanel):
			Index = 47
	class MfgSurfaceTab:
		ID = "MfgSurfaceTab"
		class WMDComponentsManagerPanel(AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 12
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 13
		class WMDComponentsPanel(AllPanels.WMDComponentsPanel):
			Index = 46
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel(AllPanels.FinishPreparePanel):
			Index = 47
	class MfgParaMeshOuterTab:
		ID = "MfgParaMeshOuterTab"
		class WMDComponentsManagerPanel(AllPanels.WMDComponentsManagerPanel):
			Index = 45
		class ParaMeshCreatePanel(AllPanels.ParaMeshCreatePanel):
			Index = 40
		class ParaMeshPreparePanel(AllPanels.ParaMeshPreparePanel):
			Index = 41
		class ParaMeshModifyPanel(AllPanels.ParaMeshModifyPanel):
			Index = 42
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 9
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class ParaMeshSelectPanel(AllPanels.ParaMeshSelectPanel):
			Index = 43
		class ParaMeshExportPanel(AllPanels.ParaMeshExportPanel):
			Index = 44
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel(AllPanels.FinishPreparePanel):
			Index = 47
	class MfgFormTab:
		ID = "MfgFormTab"
		class TSplinePrimitivePanel(AllPanels.TSplinePrimitivePanel):
			Index = 14
		class TSplineModifyPanel(AllPanels.TSplineModifyPanel):
			Index = 15
		class TSplineSymmetryPanel(AllPanels.TSplineSymmetryPanel):
			Index = 16
		class TSplineUtilitiesPanel(AllPanels.TSplineUtilitiesPanel):
			Index = 17
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class StopTSplineBaseFeaturePanel(AllPanels.StopTSplineBaseFeaturePanel):
			Index = 33
	class MfgToolsTab:
		ID = "MfgToolsTab"
		class MakePanel(AllPanels.MakePanel):
			Index = 26
		class SolidScriptsAddinsPanel(AllPanels.SolidScriptsAddinsPanel):
			Index = 27
		class UtilityPanel(AllPanels.UtilityPanel):
			Index = 28
		class ToolsInspectPanel(AllPanels.ToolsInspectPanel):
			Index = 23
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 35
		class FinishPreparePanel(AllPanels.FinishPreparePanel):
			Index = 47
	class MfgLbrPackage3DTab:
		ID = "MfgLbrPackage3DTab"
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class ReturnLibraryPanel(AllPanels.ReturnLibraryPanel):
			Index = 25
	class MfgBasefeatureSolidTab:
		ID = "MfgBasefeatureSolidTab"
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 4
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 6
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class StopBaseFeaturePanel(AllPanels.StopBaseFeaturePanel):
			Index = 32
	class MfgBasefeatureSurfaceTab:
		ID = "MfgBasefeatureSurfaceTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 12
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 13
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 20
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class StopBaseFeaturePanel(AllPanels.StopBaseFeaturePanel):
			Index = 32
	class MfgSketchTab:
		ID = "MfgSketchTab"
		class SketchCreatePanel(AllPanels.SketchCreatePanel):
			Index = 0
		class SketchModifyPanel(AllPanels.SketchModifyPanel):
			Index = 2
		class SketchConstraintsPanel(AllPanels.SketchConstraintsPanel):
			Index = 3
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class InsertPanel(AllPanels.InsertPanel):
			Index = 24
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class StopSketchPanel(AllPanels.StopSketchPanel):
			Index = 31
	class MfgEditSnapshotTab:
		ID = "MfgEditSnapshotTab"
		class SnapshotSolidModifyPanel(AllPanels.SnapshotSolidModifyPanel):
			Index = 37
		class InspectPanel(AllPanels.InspectPanel):
			Index = 21
		class SelectPanel(AllPanels.SelectPanel):
			Index = 29
		class FinishSnapshotEditPanel(AllPanels.FinishSnapshotEditPanel):
			Index = 36
	class Animation:
		ID = "Animation"
		class StoryboardPanel(AllPanels.StoryboardPanel):
			Index = 0
		class ComponentPanel(AllPanels.ComponentPanel):
			Index = 1
		class AnnotationPanel(AllPanels.AnnotationPanel):
			Index = 2
		class PublisherViewPanel(AllPanels.PublisherViewPanel):
			Index = 3
		class PublishVideoPanel(AllPanels.PublishVideoPanel):
			Index = 4
	class SolidTab:
		ID = "SolidTab"
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 7
		class GeneratePanel(AllPanels.GeneratePanel):
			Index = 8
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 9
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 44
		class PolyhedraGenerator(AllPanels.PolyhedraGenerator):
			Index = 65
		class HexNutGenerator(AllPanels.HexNutGenerator):
			Index = 66
	class SurfaceTab:
		ID = "SurfaceTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 15
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 16
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 44
	class ParaMeshOuterTab:
		ID = "ParaMeshOuterTab"
		class ParaMeshCreatePanel(AllPanels.ParaMeshCreatePanel):
			Index = 57
		class ParaMeshPreparePanel(AllPanels.ParaMeshPreparePanel):
			Index = 58
		class ParaMeshModifyPanel(AllPanels.ParaMeshModifyPanel):
			Index = 59
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class ParaMeshSelectPanel(AllPanels.ParaMeshSelectPanel):
			Index = 60
		class ParaMeshExportPanel(AllPanels.ParaMeshExportPanel):
			Index = 61
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 44
	class FormTab:
		ID = "FormTab"
		class TSplinePrimitivePanel(AllPanels.TSplinePrimitivePanel):
			Index = 17
		class TSplineModifyPanel(AllPanels.TSplineModifyPanel):
			Index = 18
		class TSplineSymmetryPanel(AllPanels.TSplineSymmetryPanel):
			Index = 19
		class TSplineUtilitiesPanel(AllPanels.TSplineUtilitiesPanel):
			Index = 20
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopTSplineBaseFeaturePanel(AllPanels.StopTSplineBaseFeaturePanel):
			Index = 42
	class SheetMetalTab:
		ID = "SheetMetalTab"
		class SheetMetalCreatePanel(AllPanels.SheetMetalCreatePanel):
			Index = 10
		class SheetMetalModifyPanel(AllPanels.SheetMetalModifyPanel):
			Index = 11
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class SheetmetalRefoldPanel(AllPanels.SheetmetalRefoldPanel):
			Index = 47
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 44
	class ToolsTab:
		ID = "ToolsTab"
		class MakePanel(AllPanels.MakePanel):
			Index = 35
		class NESTPanel(AllPanels.NESTPanel):
			Index = 56
		class SolidScriptsAddinsPanel(AllPanels.SolidScriptsAddinsPanel):
			Index = 36
		class UtilityPanel(AllPanels.UtilityPanel):
			Index = 37
		class ToolsInspectPanel(AllPanels.ToolsInspectPanel):
			Index = 29
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class SnapshotPanel(AllPanels.SnapshotPanel):
			Index = 44
		class thomasa88_anyShortcutPanel(AllPanels.thomasa88_anyShortcutPanel):
			Index = 63
		class NewPanel(AllPanels.NewPanel):
			Index = 64
	class ManageTab:
		ID = "ManageTab"
		class AssignPanel(AllPanels.AssignPanel):
			Index = 54
		class ReleasePanel(AllPanels.ReleasePanel):
			Index = 55
	class PCBTab:
		ID = "PCBTab"
		class PCBCreatePanel(AllPanels.PCBCreatePanel):
			Index = 23
		class PCBModifyPanel(AllPanels.PCBModifyPanel):
			Index = 24
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopPCBPanel(AllPanels.StopPCBPanel):
			Index = 48
	class PCB3DTab:
		ID = "PCB3DTab"
		class PCB3DPanel(AllPanels.PCB3DPanel):
			Index = 25
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
	class Package3DTab:
		ID = "Package3DTab"
		class Package3DPanel(AllPanels.Package3DPanel):
			Index = 34
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopPackagePanel(AllPanels.StopPackagePanel):
			Index = 31
	class LbrPackage3DTab:
		ID = "LbrPackage3DTab"
		class PackagePanel(AllPanels.PackagePanel):
			Index = 33
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class ReturnLibraryPanel(AllPanels.ReturnLibraryPanel):
			Index = 32
	class BasefeatureSolidTab:
		ID = "BasefeatureSolidTab"
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 7
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 9
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel(AllPanels.StopBaseFeaturePanel):
			Index = 41
	class BasefeatureSurfaceTab:
		ID = "BasefeatureSurfaceTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 15
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 16
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel(AllPanels.StopBaseFeaturePanel):
			Index = 41
	class SketchTab:
		ID = "SketchTab"
		class SketchCreatePanel(AllPanels.SketchCreatePanel):
			Index = 3
		class SketchModifyPanel(AllPanels.SketchModifyPanel):
			Index = 5
		class SketchConstraintsPanel(AllPanels.SketchConstraintsPanel):
			Index = 6
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopSketchPanel(AllPanels.StopSketchPanel):
			Index = 40
	class EditSnapshotTab:
		ID = "EditSnapshotTab"
		class SnapshotSolidModifyPanel(AllPanels.SnapshotSolidModifyPanel):
			Index = 46
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class FinishSnapshotEditPanel(AllPanels.FinishSnapshotEditPanel):
			Index = 45
	class PCBSketchTab:
		ID = "PCBSketchTab"
		class PCB3DSketchCreatePanel(AllPanels.PCB3DSketchCreatePanel):
			Index = 4
		class SketchModifyPanel(AllPanels.SketchModifyPanel):
			Index = 5
		class SketchConstraintsPanel(AllPanels.SketchConstraintsPanel):
			Index = 6
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class InsertPanel(AllPanels.InsertPanel):
			Index = 30
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopSketchPanel(AllPanels.StopSketchPanel):
			Index = 40
	class PCBBasefeatureSolidTab:
		ID = "PCBBasefeatureSolidTab"
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class SelectPanel(AllPanels.SelectPanel):
			Index = 38
		class StopBaseFeaturePanel(AllPanels.StopBaseFeaturePanel):
			Index = 41
	class RenderTab:
		ID = "RenderTab"
		class RenderSetupPanel(AllPanels.RenderSetupPanel):
			Index = 50
		class InCanvasRenderPanel(AllPanels.InCanvasRenderPanel):
			Index = 51
		class RenderPanel(AllPanels.RenderPanel):
			Index = 52
	class ParaMeshBaseFeatureTab:
		ID = "ParaMeshBaseFeatureTab"
		class ParaMeshPreparePanel(AllPanels.ParaMeshPreparePanel):
			Index = 58
		class ParaMeshModifyPanel(AllPanels.ParaMeshModifyPanel):
			Index = 59
		class AssemblePanel(AllPanels.AssemblePanel):
			Index = 12
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 26
		class InspectPanel(AllPanels.InspectPanel):
			Index = 27
		class ParaMeshSelectPanel(AllPanels.ParaMeshSelectPanel):
			Index = 60
		class ParaMeshExportPanel(AllPanels.ParaMeshExportPanel):
			Index = 61
		class ParaMeshBaseFeatureStopPanel(AllPanels.ParaMeshBaseFeatureStopPanel):
			Index = 62
	class FusionDocTab:
		ID = "FusionDocTab"
		class ViewsPanel(AllPanels.ViewsPanel):
			Index = 0
		class DrawingPanel(AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel(AllPanels.ModifyPanel):
			Index = 2
		class GeometryPanel(AllPanels.GeometryPanel):
			Index = 3
		class DimensionsPanel(AllPanels.DimensionsPanel):
			Index = 4
		class TextPanel(AllPanels.TextPanel):
			Index = 5
		class InspectPanel(AllPanels.InspectPanel):
			Index = 6
		class SymbolsPanel(AllPanels.SymbolsPanel):
			Index = 7
		class InsertPanel(AllPanels.InsertPanel):
			Index = 8
		class BillOfMaterialsPanel(AllPanels.BillOfMaterialsPanel):
			Index = 9
		class BlockPanel(AllPanels.BlockPanel):
			Index = 10
		class StopSketchEditPanel(AllPanels.StopSketchEditPanel):
			Index = 13
		class OutputPanel(AllPanels.OutputPanel):
			Index = 14
	class ManageTab:
		ID = "ManageTab"
		class AssignPanel(AllPanels.AssignPanel):
			Index = 15
		class ReleasePanel(AllPanels.ReleasePanel):
			Index = 16
	class TitleBlockTab:
		ID = "TitleBlockTab"
		class DrawingPanel(AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel(AllPanels.ModifyPanel):
			Index = 2
		class TextPanel(AllPanels.TextPanel):
			Index = 5
		class InspectPanel(AllPanels.InspectPanel):
			Index = 6
		class InsertPanel(AllPanels.InsertPanel):
			Index = 8
		class StopBlockEditPanel(AllPanels.StopBlockEditPanel):
			Index = 11
	class BorderTab:
		ID = "BorderTab"
		class DrawingPanel(AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel(AllPanels.ModifyPanel):
			Index = 2
		class TextPanel(AllPanels.TextPanel):
			Index = 5
		class InspectPanel(AllPanels.InspectPanel):
			Index = 6
		class InsertPanel(AllPanels.InsertPanel):
			Index = 8
		class StopBorderEditPanel(AllPanels.StopBorderEditPanel):
			Index = 12
	class SketchTab:
		ID = "SketchTab"
		class DrawingPanel(AllPanels.DrawingPanel):
			Index = 1
		class ModifyPanel(AllPanels.ModifyPanel):
			Index = 2
		class TextPanel(AllPanels.TextPanel):
			Index = 5
		class InspectPanel(AllPanels.InspectPanel):
			Index = 6
		class InsertPanel(AllPanels.InsertPanel):
			Index = 8
		class StopSketchEditPanel(AllPanels.StopSketchEditPanel):
			Index = 13
	class GenSolidTab:
		ID = "GenSolidTab"
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 0
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 1
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class EditModelSelectPanel(AllPanels.EditModelSelectPanel):
			Index = 17
		class FinishEditModelPanel(AllPanels.FinishEditModelPanel):
			Index = 18
	class GenSurfaceTab:
		ID = "GenSurfaceTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 3
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 4
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class EditModelSelectPanel(AllPanels.EditModelSelectPanel):
			Index = 17
		class FinishEditModelPanel(AllPanels.FinishEditModelPanel):
			Index = 18
	class GenSketchTab:
		ID = "GenSketchTab"
		class SketchCreatePanel(AllPanels.SketchCreatePanel):
			Index = 10
		class SketchModifyPanel(AllPanels.SketchModifyPanel):
			Index = 11
		class SketchConstraintsPanel(AllPanels.SketchConstraintsPanel):
			Index = 12
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class InsertPanel(AllPanels.InsertPanel):
			Index = 9
		class SelectPanel(AllPanels.SelectPanel):
			Index = 8
		class StopSketchPanel(AllPanels.StopSketchPanel):
			Index = 13
	class SimSolidTab:
		ID = "SimSolidTab"
		class SolidCreatePanel(AllPanels.SolidCreatePanel):
			Index = 0
		class SolidModifyPanel(AllPanels.SolidModifyPanel):
			Index = 1
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel(AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel(AllPanels.FinishSimplifyPanel):
			Index = 18
	class SimSurfaceTab:
		ID = "SimSurfaceTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 3
		class SurfaceModifyPanel(AllPanels.SurfaceModifyPanel):
			Index = 4
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel(AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel(AllPanels.FinishSimplifyPanel):
			Index = 18
	class IdealizeTab:
		ID = "IdealizeTab"
		class SurfaceCreatePanel(AllPanels.SurfaceCreatePanel):
			Index = 3
		class IdealizeModifyPanel(AllPanels.IdealizeModifyPanel):
			Index = 5
		class ShellsPanel(AllPanels.ShellsPanel):
			Index = 6
		class ConstructionPanel(AllPanels.ConstructionPanel):
			Index = 2
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class SimplifySelectPanel(AllPanels.SimplifySelectPanel):
			Index = 17
		class FinishSimplifyPanel(AllPanels.FinishSimplifyPanel):
			Index = 18
	class SketchTab:
		ID = "SketchTab"
		class SketchCreatePanel(AllPanels.SketchCreatePanel):
			Index = 10
		class SketchModifyPanel(AllPanels.SketchModifyPanel):
			Index = 11
		class SketchConstraintsPanel(AllPanels.SketchConstraintsPanel):
			Index = 12
		class SketchInspectPanel(AllPanels.SketchInspectPanel):
			Index = 7
		class InsertPanel(AllPanels.InsertPanel):
			Index = 9
		class SelectPanel(AllPanels.SelectPanel):
			Index = 8
		class StopSketchPanel(AllPanels.StopSketchPanel):
			Index = 13
	class ToolsTab:
		ID = "ToolsTab"
		class ReturnPanel(AllPanels.ReturnPanel):
			Index = 19
	class SimSetupTab:
		ID = "SimSetupTab"
		class StudyPanel(AllPanels.StudyPanel):
			Index = 12
		class SimplifyPanel(AllPanels.SimplifyPanel):
			Index = 13
		class MaterialsPanel(AllPanels.MaterialsPanel):
			Index = 14
		class ConstraintsPanel(AllPanels.ConstraintsPanel):
			Index = 26
		class LoadsPanel(AllPanels.LoadsPanel):
			Index = 27
		class ContactsPanel(AllPanels.ContactsPanel):
			Index = 28
		class DisplayPanel(AllPanels.DisplayPanel):
			Index = 15
		class OptimizationPanel(AllPanels.OptimizationPanel):
			Index = 29
		class ManagePanel(AllPanels.ManagePanel):
			Index = 5
		class SolvePanel(AllPanels.SolvePanel):
			Index = 3
		class AnsysPanel(AllPanels.AnsysPanel):
			Index = 4
		class ResultsCmdPanel(AllPanels.ResultsCmdPanel):
			Index = 31
		class InspectPanel(AllPanels.InspectPanel):
			Index = 18
		class SelectPanel(AllPanels.SelectPanel):
			Index = 20
	class SimResultsTab:
		ID = "SimResultsTab"
		class ResultToolsPanel(AllPanels.ResultToolsPanel):
			Index = 0
		class ComparePanel(AllPanels.ComparePanel):
			Index = 1
		class DeformationPanel(AllPanels.DeformationPanel):
			Index = 2
		class ResultsDisplayPanel(AllPanels.ResultsDisplayPanel):
			Index = 16
		class ResultsManagePanel(AllPanels.ResultsManagePanel):
			Index = 6
		class ResultsInspectPanel(AllPanels.ResultsInspectPanel):
			Index = 19
		class SelectPanel(AllPanels.SelectPanel):
			Index = 20
		class FinishResultsPanel(AllPanels.FinishResultsPanel):
			Index = 22
	class CompareTab:
		ID = "CompareTab"
		class SynchronizePanel(AllPanels.SynchronizePanel):
			Index = 7
		class ResultsAnimatePanel(AllPanels.ResultsAnimatePanel):
			Index = 8
		class ResultsOptionsPanel(AllPanels.ResultsOptionsPanel):
			Index = 9
		class CompareLayoutsPanel(AllPanels.CompareLayoutsPanel):
			Index = 10
		class PostMeshPanel(AllPanels.PostMeshPanel):
			Index = 11
		class FinishSimComparePanel(AllPanels.FinishSimComparePanel):
			Index = 21
class Toolbars:
	class ActiveDocumentsToolbar:
		ID = "ActiveDocumentsToolbar"
	class ActiveViewToolbar:
		ID = "ActiveViewToolbar"
	class EIPToolbar:
		ID = "EIPToolbar"
	class ElectronNavToolbar:
		ID = "Electron::NavToolbar"
	class ElectronicDesignNavToolbar:
		ID = "ElectronicDesign::NavToolbar"
	class FusionDocNavToolbar:
		ID = "FusionDocNavToolbar"
	class MessageTray:
		ID = "MessageTray"
	class NavToolbar:
		ID = "NavToolbar"
	class QAT:
		ID = "QAT"
	class QATRight:
		ID = "QATRight"
class WorkSpaces:
	class FusionSolidEnvironment:
		ID = "FusionSolidEnvironment"
		class Tabs:
			class SolidTab(AllTabs.SolidTab):
				Index = 0
			class SurfaceTab(AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab(AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab(AllTabs.FormTab):
				Index = 2
			class SheetMetalTab(AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab(AllTabs.ToolsTab):
				Index = 4
			class ManageTab(AllTabs.ManageTab):
				Index = 5
			class PCBTab(AllTabs.PCBTab):
				Index = 6
			class Package3DTab(AllTabs.Package3DTab):
				Index = 8
			class BasefeatureSolidTab(AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab(AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab(AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab(AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab(AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCB3DSketchCreatePanel = AllPanels.PCB3DSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCB3DPanel = AllPanels.PCB3DPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			Package3DPanel = AllPanels.Package3DPanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
			PolyhedraGenerator = AllPanels.PolyhedraGenerator
			HexNutGenerator = AllPanels.HexNutGenerator
	class GenerativeEnvironment:
		ID = "GenerativeEnvironment"
		class Tabs:
			class DefineTab(AllTabs.DefineTab):
				Index = 0
			class ExploreTab(AllTabs.ExploreTab):
				Index = 1
			class OutcomeViewTab(AllTabs.OutcomeViewTab):
				Index = 2
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			GenStudyPanel1 = AllPanels.GenStudyPanel1
			GenModelPanel = AllPanels.GenModelPanel
			GuidePanel = AllPanels.GuidePanel
			GenDesignSpacePanel = AllPanels.GenDesignSpacePanel
			GenDesignConditionsPanel = AllPanels.GenDesignConditionsPanel
			GenDesignCriteriaPanel = AllPanels.GenDesignCriteriaPanel
			GenMaterialsPanel = AllPanels.GenMaterialsPanel
			GenSolvePanel = AllPanels.GenSolvePanel
			GenExplore = AllPanels.GenExplore
			ExploreDisplayPanel = AllPanels.ExploreDisplayPanel
			ExploreDesignSpaceViewPanel = AllPanels.ExploreDesignSpaceViewPanel
			ExploreComparePanel = AllPanels.ExploreComparePanel
			ExploreExportPanel = AllPanels.ExploreExportPanel
			ExploreExportDataPanel = AllPanels.ExploreExportDataPanel
			ExploreTagPanel = AllPanels.ExploreTagPanel
			FinishOutcomeViewPanel = AllPanels.FinishOutcomeViewPanel
			FinishExplorePanel = AllPanels.FinishExplorePanel
			GenInspectPanel = AllPanels.GenInspectPanel
			GenSelectPanel = AllPanels.GenSelectPanel
	class PCBEnvironment:
		ID = "PCBEnvironment"
		class Tabs:
			class SolidTab(AllTabs.SolidTab):
				Index = 0
			class SurfaceTab(AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab(AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab(AllTabs.FormTab):
				Index = 2
			class SheetMetalTab(AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab(AllTabs.ToolsTab):
				Index = 4
			class ManageTab(AllTabs.ManageTab):
				Index = 5
			class PCBTab(AllTabs.PCBTab):
				Index = 6
			class Package3DTab(AllTabs.Package3DTab):
				Index = 8
			class BasefeatureSolidTab(AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab(AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab(AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab(AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab(AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCB3DSketchCreatePanel = AllPanels.PCB3DSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCB3DPanel = AllPanels.PCB3DPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			Package3DPanel = AllPanels.Package3DPanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
			PolyhedraGenerator = AllPanels.PolyhedraGenerator
			HexNutGenerator = AllPanels.HexNutGenerator
	class PCB3DEnvironment:
		ID = "PCB3DEnvironment"
		class Tabs:
			class PCB3DTab(AllTabs.PCB3DTab):
				Index = 7
			class PCBSketchTab(AllTabs.PCBSketchTab):
				Index = 14
			class PCBBasefeatureSolidTab(AllTabs.PCBBasefeatureSolidTab):
				Index = 15
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCB3DSketchCreatePanel = AllPanels.PCB3DSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCB3DPanel = AllPanels.PCB3DPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			Package3DPanel = AllPanels.Package3DPanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
			PolyhedraGenerator = AllPanels.PolyhedraGenerator
			HexNutGenerator = AllPanels.HexNutGenerator
	class Package3DEnvironment:
		ID = "Package3DEnvironment"
		class Tabs:
			class SolidTab(AllTabs.SolidTab):
				Index = 0
			class SurfaceTab(AllTabs.SurfaceTab):
				Index = 1
			class ParaMeshOuterTab(AllTabs.ParaMeshOuterTab):
				Index = 18
			class FormTab(AllTabs.FormTab):
				Index = 2
			class SheetMetalTab(AllTabs.SheetMetalTab):
				Index = 3
			class ToolsTab(AllTabs.ToolsTab):
				Index = 4
			class ManageTab(AllTabs.ManageTab):
				Index = 5
			class PCBTab(AllTabs.PCBTab):
				Index = 6
			class Package3DTab(AllTabs.Package3DTab):
				Index = 8
			class BasefeatureSolidTab(AllTabs.BasefeatureSolidTab):
				Index = 10
			class BasefeatureSurfaceTab(AllTabs.BasefeatureSurfaceTab):
				Index = 11
			class SketchTab(AllTabs.SketchTab):
				Index = 12
			class EditSnapshotTab(AllTabs.EditSnapshotTab):
				Index = 13
			class ParaMeshBaseFeatureTab(AllTabs.ParaMeshBaseFeatureTab):
				Index = 19
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCB3DSketchCreatePanel = AllPanels.PCB3DSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCB3DPanel = AllPanels.PCB3DPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			Package3DPanel = AllPanels.Package3DPanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
			PolyhedraGenerator = AllPanels.PolyhedraGenerator
			HexNutGenerator = AllPanels.HexNutGenerator
	class FusionRenderEnvironment:
		ID = "FusionRenderEnvironment"
		class Tabs:
			class RenderTab(AllTabs.RenderTab):
				Index = 16
		class Panels:
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			SketchCreatePanel = AllPanels.SketchCreatePanel
			PCB3DSketchCreatePanel = AllPanels.PCB3DSketchCreatePanel
			SketchModifyPanel = AllPanels.SketchModifyPanel
			SketchConstraintsPanel = AllPanels.SketchConstraintsPanel
			SolidCreatePanel = AllPanels.SolidCreatePanel
			GeneratePanel = AllPanels.GeneratePanel
			SolidModifyPanel = AllPanels.SolidModifyPanel
			SheetMetalCreatePanel = AllPanels.SheetMetalCreatePanel
			SheetMetalModifyPanel = AllPanels.SheetMetalModifyPanel
			AssemblePanel = AllPanels.AssemblePanel
			AssembleModifyPanel = AllPanels.AssembleModifyPanel
			AssembleUtilityPanel = AllPanels.AssembleUtilityPanel
			SurfaceCreatePanel = AllPanels.SurfaceCreatePanel
			SurfaceModifyPanel = AllPanels.SurfaceModifyPanel
			TSplinePrimitivePanel = AllPanels.TSplinePrimitivePanel
			TSplineModifyPanel = AllPanels.TSplineModifyPanel
			TSplineSymmetryPanel = AllPanels.TSplineSymmetryPanel
			TSplineUtilitiesPanel = AllPanels.TSplineUtilitiesPanel
			MeshPrimitivePanel = AllPanels.MeshPrimitivePanel
			MeshModifyPanel = AllPanels.MeshModifyPanel
			PCBCreatePanel = AllPanels.PCBCreatePanel
			PCBModifyPanel = AllPanels.PCBModifyPanel
			PCB3DPanel = AllPanels.PCB3DPanel
			ConstructionPanel = AllPanels.ConstructionPanel
			InspectPanel = AllPanels.InspectPanel
			InspectMeshPanel = AllPanels.InspectMeshPanel
			ToolsInspectPanel = AllPanels.ToolsInspectPanel
			InsertPanel = AllPanels.InsertPanel
			StopPackagePanel = AllPanels.StopPackagePanel
			ReturnLibraryPanel = AllPanels.ReturnLibraryPanel
			PackagePanel = AllPanels.PackagePanel
			Package3DPanel = AllPanels.Package3DPanel
			MakePanel = AllPanels.MakePanel
			SolidScriptsAddinsPanel = AllPanels.SolidScriptsAddinsPanel
			UtilityPanel = AllPanels.UtilityPanel
			SelectPanel = AllPanels.SelectPanel
			NewPanel = AllPanels.NewPanel
			MeshSelectPanel = AllPanels.MeshSelectPanel
			StopSketchPanel = AllPanels.StopSketchPanel
			StopBaseFeaturePanel = AllPanels.StopBaseFeaturePanel
			StopTSplineBaseFeaturePanel = AllPanels.StopTSplineBaseFeaturePanel
			StopMeshBaseFeaturePanel = AllPanels.StopMeshBaseFeaturePanel
			SnapshotPanel = AllPanels.SnapshotPanel
			FinishSnapshotEditPanel = AllPanels.FinishSnapshotEditPanel
			SnapshotSolidModifyPanel = AllPanels.SnapshotSolidModifyPanel
			SheetmetalRefoldPanel = AllPanels.SheetmetalRefoldPanel
			StopPCBPanel = AllPanels.StopPCBPanel
			ReturnPanel = AllPanels.ReturnPanel
			RenderSetupPanel = AllPanels.RenderSetupPanel
			InCanvasRenderPanel = AllPanels.InCanvasRenderPanel
			RenderPanel = AllPanels.RenderPanel
			ToolsPanel = AllPanels.ToolsPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
			NESTPanel = AllPanels.NESTPanel
			ParaMeshCreatePanel = AllPanels.ParaMeshCreatePanel
			ParaMeshPreparePanel = AllPanels.ParaMeshPreparePanel
			ParaMeshModifyPanel = AllPanels.ParaMeshModifyPanel
			ParaMeshSelectPanel = AllPanels.ParaMeshSelectPanel
			ParaMeshExportPanel = AllPanels.ParaMeshExportPanel
			ParaMeshBaseFeatureStopPanel = AllPanels.ParaMeshBaseFeatureStopPanel
			thomasa88_anyShortcutPanel = AllPanels.thomasa88_anyShortcutPanel
			PolyhedraGenerator = AllPanels.PolyhedraGenerator
			HexNutGenerator = AllPanels.HexNutGenerator
	class Publisher3DEnvironment:
		ID = "Publisher3DEnvironment"
		class Tabs:
			class Animation(AllTabs.Animation):
				Index = 0
		class Panels:
			StoryboardPanel = AllPanels.StoryboardPanel
			ComponentPanel = AllPanels.ComponentPanel
			AnnotationPanel = AllPanels.AnnotationPanel
			PublisherViewPanel = AllPanels.PublisherViewPanel
			PublishVideoPanel = AllPanels.PublishVideoPanel
	class SimulationEnvironment:
		ID = "SimulationEnvironment"
		class Tabs:
			class SimSetupTab(AllTabs.SimSetupTab):
				Index = 0
			class SimResultsTab(AllTabs.SimResultsTab):
				Index = 1
			class CompareTab(AllTabs.CompareTab):
				Index = 2
		class Panels:
			ResultToolsPanel = AllPanels.ResultToolsPanel
			ComparePanel = AllPanels.ComparePanel
			DeformationPanel = AllPanels.DeformationPanel
			SolvePanel = AllPanels.SolvePanel
			AnsysPanel = AllPanels.AnsysPanel
			ManagePanel = AllPanels.ManagePanel
			ResultsManagePanel = AllPanels.ResultsManagePanel
			SynchronizePanel = AllPanels.SynchronizePanel
			ResultsAnimatePanel = AllPanels.ResultsAnimatePanel
			ResultsOptionsPanel = AllPanels.ResultsOptionsPanel
			CompareLayoutsPanel = AllPanels.CompareLayoutsPanel
			PostMeshPanel = AllPanels.PostMeshPanel
			StudyPanel = AllPanels.StudyPanel
			SimplifyPanel = AllPanels.SimplifyPanel
			MaterialsPanel = AllPanels.MaterialsPanel
			DisplayPanel = AllPanels.DisplayPanel
			ResultsDisplayPanel = AllPanels.ResultsDisplayPanel
			ResultsSolvePanel = AllPanels.ResultsSolvePanel
			InspectPanel = AllPanels.InspectPanel
			ResultsInspectPanel = AllPanels.ResultsInspectPanel
			SelectPanel = AllPanels.SelectPanel
			FinishSimComparePanel = AllPanels.FinishSimComparePanel
			FinishResultsPanel = AllPanels.FinishResultsPanel
			FilePanel = AllPanels.FilePanel
			DiagnosticsPanel = AllPanels.DiagnosticsPanel
			UIDemo = AllPanels.UIDemo
			ConstraintsPanel = AllPanels.ConstraintsPanel
			LoadsPanel = AllPanels.LoadsPanel
			ContactsPanel = AllPanels.ContactsPanel
			OptimizationPanel = AllPanels.OptimizationPanel
			ResultsPanel = AllPanels.ResultsPanel
			ResultsCmdPanel = AllPanels.ResultsCmdPanel
	class CAMEnvironment:
		ID = "CAMEnvironment"
		class Tabs:
			class MillingTab(AllTabs.MillingTab):
				Index = 0
			class TurningTab(AllTabs.TurningTab):
				Index = 1
			class AdditiveTab(AllTabs.AdditiveTab):
				Index = 2
			class AdditiveResultsTab(AllTabs.AdditiveResultsTab):
				Index = 3
			class ProbingTab(AllTabs.ProbingTab):
				Index = 4
			class FabricationTab(AllTabs.FabricationTab):
				Index = 5
			class UtilitiesTab(AllTabs.UtilitiesTab):
				Index = 6
			class PartAlignmentTab(AllTabs.PartAlignmentTab):
				Index = 7
			class LiveAlignmentTab(AllTabs.LiveAlignmentTab):
				Index = 8
			class FeaturesTab(AllTabs.FeaturesTab):
				Index = 9
		class Panels:
			CAMJobPanel = AllPanels.CAMJobPanel
			CAMInProcessStockPanel = AllPanels.CAMInProcessStockPanel
			CAMAdditiveJobPanel = AllPanels.CAMAdditiveJobPanel
			CAMAdditivePositioningPanel = AllPanels.CAMAdditivePositioningPanel
			CAM2DPanel = AllPanels.CAM2DPanel
			CAM3DPanel = AllPanels.CAM3DPanel
			CAMEditPanel = AllPanels.CAMEditPanel
			CAMDrillingPanel = AllPanels.CAMDrillingPanel
			CAMMultiAxisPanel = AllPanels.CAMMultiAxisPanel
			CAMTurningPanel = AllPanels.CAMTurningPanel
			CAMWLPCPanel = AllPanels.CAMWLPCPanel
			CAMInfillPanel = AllPanels.CAMInfillPanel
			CAMSupportsPanel = AllPanels.CAMSupportsPanel
			CAMDEDPanel = AllPanels.CAMDEDPanel
			CAMAdditiveProcessSimPanel = AllPanels.CAMAdditiveProcessSimPanel
			CAMAdditiveProcessSimResultsPanel = AllPanels.CAMAdditiveProcessSimResultsPanel
			CAMAdditiveProcessSimActionPanel = AllPanels.CAMAdditiveProcessSimActionPanel
			CAMAdditiveProcessSimFinishPanel = AllPanels.CAMAdditiveProcessSimFinishPanel
			CAMProbingPanel = AllPanels.CAMProbingPanel
			CAMCMMPanel = AllPanels.CAMCMMPanel
			CAMManualInspectionPanel = AllPanels.CAMManualInspectionPanel
			CAMPartAlignmentEditPanel = AllPanels.CAMPartAlignmentEditPanel
			CAMPartAlignmentInspectPanel = AllPanels.CAMPartAlignmentInspectPanel
			CAMPartAlignmentPostPanel = AllPanels.CAMPartAlignmentPostPanel
			CAMLiveAlignmentPostPanel = AllPanels.CAMLiveAlignmentPostPanel
			CAMPartAlignmentResultsPanel = AllPanels.CAMPartAlignmentResultsPanel
			CAMLiveAlignmentResultsPanel = AllPanels.CAMLiveAlignmentResultsPanel
			CAMPartAlignmentPostAndExitPanel = AllPanels.CAMPartAlignmentPostAndExitPanel
			CAMPartAlignmentFinishPanel = AllPanels.CAMPartAlignmentFinishPanel
			CAMLiveAlignmentFinishPanel = AllPanels.CAMLiveAlignmentFinishPanel
			CAMActionPanel = AllPanels.CAMActionPanel
			CAMProbingActionPanel = AllPanels.CAMProbingActionPanel
			CAMAdditivePrintProfilePanel = AllPanels.CAMAdditivePrintProfilePanel
			CAMAdditiveActionPanel = AllPanels.CAMAdditiveActionPanel
			CAMInspectPanel = AllPanels.CAMInspectPanel
			CAMManagePanel = AllPanels.CAMManagePanel
			CAMAdditiveManagePanel = AllPanels.CAMAdditiveManagePanel
			CAMGeometryFeatures = AllPanels.CAMGeometryFeatures
			CAMScriptsAddinsPanel = AllPanels.CAMScriptsAddinsPanel
			SelectPanel = AllPanels.SelectPanel
			ManufacturingSourcesPanel = AllPanels.ManufacturingSourcesPanel
			FabricationManagePanel = AllPanels.FabricationManagePanel
			MachineBuilderActivationPanel = AllPanels.MachineBuilderActivationPanel
			NESTPanel = AllPanels.NESTPanel
	class FusionDocumentationEnvironment:
		ID = "FusionDocumentationEnvironment"
		class Tabs:
			class FusionDocTab(AllTabs.FusionDocTab):
				Index = 0
			class ManageTab(AllTabs.ManageTab):
				Index = 1
			class TitleBlockTab(AllTabs.TitleBlockTab):
				Index = 2
			class BorderTab(AllTabs.BorderTab):
				Index = 3
			class SketchTab(AllTabs.SketchTab):
				Index = 4
		class Panels:
			ViewsPanel = AllPanels.ViewsPanel
			DrawingPanel = AllPanels.DrawingPanel
			ModifyPanel = AllPanels.ModifyPanel
			GeometryPanel = AllPanels.GeometryPanel
			DimensionsPanel = AllPanels.DimensionsPanel
			TextPanel = AllPanels.TextPanel
			InspectPanel = AllPanels.InspectPanel
			SymbolsPanel = AllPanels.SymbolsPanel
			InsertPanel = AllPanels.InsertPanel
			BillOfMaterialsPanel = AllPanels.BillOfMaterialsPanel
			BlockPanel = AllPanels.BlockPanel
			StopBlockEditPanel = AllPanels.StopBlockEditPanel
			StopBorderEditPanel = AllPanels.StopBorderEditPanel
			StopSketchEditPanel = AllPanels.StopSketchEditPanel
			OutputPanel = AllPanels.OutputPanel
			AssignPanel = AllPanels.AssignPanel
			ReleasePanel = AllPanels.ReleasePanel
	class ElectronEmptyLbrEnvironment:
		ID = "ElectronEmptyLbrEnvironment"
		class Tabs:
			class LbrEmptyTab(AllTabs.LbrEmptyTab):
				Index = 0
			class LbrDocumentTab(AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab(AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab(AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronDeviceEnvironment:
		ID = "ElectronDeviceEnvironment"
		class Tabs:
			class LbrDeviceTab(AllTabs.LbrDeviceTab):
				Index = 1
			class LbrDocumentTab(AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab(AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab(AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronFootprintEnvironment:
		ID = "ElectronFootprintEnvironment"
		class Tabs:
			class LbrFootprintTab(AllTabs.LbrFootprintTab):
				Index = 2
			class LbrDocumentTab(AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab(AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab(AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronSymbolEnvironment:
		ID = "ElectronSymbolEnvironment"
		class Tabs:
			class LbrSymbolTab(AllTabs.LbrSymbolTab):
				Index = 3
			class LbrDocumentTab(AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab(AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab(AllTabs.LbrManagementTab):
				Index = 6
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
	class ElectronPackageEnvironment:
		ID = "ElectronPackageEnvironment"
		class Tabs:
			class LbrDocumentTab(AllTabs.LbrDocumentTab):
				Index = 4
			class LbrAutomateTab(AllTabs.LbrAutomateTab):
				Index = 5
			class LbrManagementTab(AllTabs.LbrManagementTab):
				Index = 6
			class LbrPackageTab(AllTabs.LbrPackageTab):
				Index = 7
		class Panels:
			LbrCreatePanel = AllPanels.LbrCreatePanel
			LbrPackagePanel = AllPanels.LbrPackagePanel
			LbrSymbolViewPanel = AllPanels.LbrSymbolViewPanel
			LbrSymbolLayersPanel = AllPanels.LbrSymbolLayersPanel
			LbrSymbolPlacePanel = AllPanels.LbrSymbolPlacePanel
			LbrSymbolEditPanel = AllPanels.LbrSymbolEditPanel
			LbrSymbolModifyPanel = AllPanels.LbrSymbolModifyPanel
			LbrSymbolDrawPanel = AllPanels.LbrSymbolDrawPanel
			LbrSymbolSelectPanel = AllPanels.LbrSymbolSelectPanel
			LbrFootprintViewPanel = AllPanels.LbrFootprintViewPanel
			LbrFootprintLayersPanel = AllPanels.LbrFootprintLayersPanel
			LbrFootprintCreatePanel = AllPanels.LbrFootprintCreatePanel
			LbrFootprintEditPanel = AllPanels.LbrFootprintEditPanel
			LbrFootprintModifyPanel = AllPanels.LbrFootprintModifyPanel
			LbrFootprintDrawPanel = AllPanels.LbrFootprintDrawPanel
			LbrFootprintSelectPanel = AllPanels.LbrFootprintSelectPanel
			LbrDevicePanel = AllPanels.LbrDevicePanel
			LbrDeviceModifyPanel = AllPanels.LbrDeviceModifyPanel
			LbrSymModelPanel = AllPanels.LbrSymModelPanel
			LbrDeviceSelectPanel = AllPanels.LbrDeviceSelectPanel
			LbrDrawCommonPanel = AllPanels.LbrDrawCommonPanel
			LbrLibraryioPanel = AllPanels.LbrLibraryioPanel
			LbrOutputPanel = AllPanels.LbrOutputPanel
			LbrAutomatePanel = AllPanels.LbrAutomatePanel
			LbrManagementPanel = AllPanels.LbrManagementPanel
